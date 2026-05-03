import os
import time
import json
import threading
import urllib.request
import urllib.parse
import feedparser
from flask import Flask, render_template, redirect, url_for, request, abort
from feeds import SPORTS_CONFIG, score_article, LATAM_CONFIG, MERCADO_VALOR
from articulos import ARTICULOS, get_articulo

app = Flask(__name__)

_cache = {}
_cache_lock = threading.Lock()
CACHE_TTL = 30 * 60  # 30 minutos


def _extract_image(e):
    if hasattr(e, 'media_thumbnail') and e.media_thumbnail:
        return e.media_thumbnail[0].get('url', '')
    if hasattr(e, 'media_content') and e.media_content:
        for mc in e.media_content:
            url = mc.get('url', '')
            if url:
                return url
    if hasattr(e, 'enclosures') and e.enclosures:
        for enc in e.enclosures:
            if enc.get('type', '').startswith('image') and enc.get('href'):
                return enc['href']
    return ''


def _fetch_feed(url):
    with _cache_lock:
        if url in _cache:
            ts, data = _cache[url]
            if time.time() - ts < CACHE_TTL:
                return data
    try:
        feed = feedparser.parse(url)
        entries = []
        for e in feed.entries[:15]:
            source = ''
            if hasattr(e, 'source'):
                source = getattr(e.source, 'title', '')
            if not source:
                source = url.split('/')[2].replace('www.', '').replace('news.google.com', 'Google News')
            entries.append({
                'title': e.get('title', '').strip(),
                'summary': _clean(e.get('summary', '')),
                'link': e.get('link', '#'),
                'source': source,
                'published': e.get('published', ''),
                'image': _extract_image(e),
            })
        with _cache_lock:
            _cache[url] = (time.time(), entries)
        return entries
    except Exception:
        return []


def _clean(text):
    import re
    import html
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:220] + '…' if len(text) > 220 else text


def get_articles(sport_key, limit=25):
    config = SPORTS_CONFIG.get(sport_key)
    if not config:
        return []
    raw = []
    for url in config['feeds']:
        raw.extend(_fetch_feed(url))

    seen, unique = set(), []
    for a in raw:
        key = a['title'][:60]
        if key and key not in seen:
            seen.add(key)
            a['score'] = score_article(a['title'], a['summary'])
            a['sport_key'] = sport_key
            a['sport_name'] = config['name']
            a['sport_color'] = config['color']
            a['sport_emoji'] = config['emoji']
            unique.append(a)
    return unique[:limit]


def get_player_wiki(nombre):
    encoded = urllib.parse.quote(nombre)
    url = f'https://es.wikipedia.org/api/rest_v1/page/summary/{encoded}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'DeportesMundo/1.0'})
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode())
        return {
            'name': data.get('title', nombre),
            'bio': data.get('extract', ''),
            'image': data.get('thumbnail', {}).get('source', ''),
            'wiki_url': data.get('content_urls', {}).get('desktop', {}).get('page', ''),
            'found': True,
        }
    except Exception:
        return {'name': nombre, 'bio': '', 'image': '', 'wiki_url': '', 'found': False}


def get_espn_standings(slug):
    url = f'https://site.api.espn.com/apis/v2/sports/soccer/{slug}/standings'
    with _cache_lock:
        if url in _cache:
            ts, data = _cache[url]
            if time.time() - ts < CACHE_TTL:
                return data
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'DeportesMundo/1.0'})
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode())
        rows = []
        entries = data.get('standings', {}).get('entries', [])
        if not entries:
            children = data.get('children', [])
            if children:
                entries = children[0].get('standings', {}).get('entries', [])
        for entry in entries[:20]:
            team = entry.get('team', {})
            stats = {s['name']: s.get('displayValue', '-') for s in entry.get('stats', [])}
            logos = team.get('logos', [])
            rows.append({
                'pos': stats.get('rank', str(entry.get('rank', '-'))),
                'team': team.get('displayName', '?'),
                'logo': logos[0].get('href', '') if logos else '',
                'pj': stats.get('gamesPlayed', '-'),
                'pts': stats.get('points', '-'),
                'gf': stats.get('pointsFor', '-'),
                'gc': stats.get('pointsAgainst', '-'),
            })
        with _cache_lock:
            _cache[url] = (time.time(), rows)
        return rows
    except Exception:
        return []


def get_latam_news(liga_cfg, limit=5):
    articles = []
    for feed_url in liga_cfg.get('feeds', []):
        for e in _fetch_feed(feed_url)[:limit]:
            e['score'] = score_article(e['title'], e['summary'])
            articles.append(e)
    seen, unique = set(), []
    for a in articles:
        k = a['title'][:60]
        if k not in seen:
            seen.add(k)
            unique.append(a)
    return unique[:limit]


# ─── Rutas ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    all_articles = []
    for sport_key in SPORTS_CONFIG:
        all_articles.extend(get_articles(sport_key, limit=6))

    top = sorted(all_articles, key=lambda x: x['score'], reverse=True)[:12]
    monetizable = [a for a in all_articles if a['score'] >= 2][:10]
    recientes = sorted(all_articles, key=lambda x: x.get('published', ''), reverse=True)[:16]

    return render_template('index.html',
        sports=SPORTS_CONFIG,
        top=top,
        monetizable=monetizable,
        recientes=recientes,
        current_sport=None,
    )


@app.route('/deporte/<sport_key>')
def sport_page(sport_key):
    if sport_key not in SPORTS_CONFIG:
        return redirect(url_for('index'))
    config = SPORTS_CONFIG[sport_key]
    articles = get_articles(sport_key, limit=30)
    top = sorted(articles, key=lambda x: x['score'], reverse=True)[:8]
    monetizable = [a for a in articles if a['score'] >= 2]

    return render_template('sport.html',
        sports=SPORTS_CONFIG,
        config=config,
        sport_key=sport_key,
        articles=articles,
        top=top,
        monetizable=monetizable,
        current_sport=sport_key,
    )


@app.route('/futbol-latam')
def futbol_latam():
    data = {}
    for conf_key, conf in LATAM_CONFIG.items():
        data[conf_key] = {'config': conf, 'ligas': {}}
        for liga_key, liga in conf['ligas'].items():
            news = get_latam_news(liga, limit=5)
            standings = get_espn_standings(liga['espn_slug']) if liga.get('espn_slug') else []
            data[conf_key]['ligas'][liga_key] = {
                'config': liga,
                'news': news,
                'standings': standings,
            }
    return render_template('latam.html',
        sports=SPORTS_CONFIG,
        latam=data,
        latam_config=LATAM_CONFIG,
        mercado=MERCADO_VALOR,
        current_sport='futbol',
    )


@app.route('/jugador/<path:nombre>')
def jugador(nombre):
    player = get_player_wiki(nombre)
    sport_key = request.args.get('deporte', 'futbol')
    config = SPORTS_CONFIG.get(sport_key, SPORTS_CONFIG['futbol'])
    content_ideas = _content_ideas(player['name'], player['bio'])
    valor = MERCADO_VALOR.get(player['name'], None)

    return render_template('jugador.html',
        sports=SPORTS_CONFIG,
        player=player,
        sport_key=sport_key,
        config=config,
        content_ideas=content_ideas,
        valor=valor,
        current_sport=sport_key,
    )


def _content_ideas(name, bio):
    ideas = [
        f'La historia de vida de {name}: de sus inicios al estrellato',
        f'Los 5 momentos más épicos de {name}',
        f'{name}: curiosidades que no sabías',
        f'El legado de {name} en el deporte mundial',
        f'¿Cuánto gana {name}? Fortuna y negocios',
        f'{name} vs sus rivales históricos: el debate eterno',
        f'La vida personal de {name}: familia, hobbies y más',
    ]
    return ideas


@app.route('/buscar')
def buscar():
    query = request.args.get('q', '').strip()
    results = []
    if query:
        terms = query.lower().split()
        for sport_key in SPORTS_CONFIG:
            for a in get_articles(sport_key, limit=30):
                text = (a['title'] + ' ' + a.get('summary', '')).lower()
                if all(t in text for t in terms):
                    results.append(a)
        results.sort(key=lambda x: x['score'], reverse=True)
    return render_template('buscar.html',
        sports=SPORTS_CONFIG,
        query=query,
        results=results,
        current_sport=None,
    )


@app.route('/articulos')
def articulos():
    return render_template('articulos.html',
        sports=SPORTS_CONFIG,
        articulos=ARTICULOS,
        current_sport=None,
    )


@app.route('/articulo/<slug>')
def articulo(slug):
    art = get_articulo(slug)
    if not art:
        return redirect(url_for('articulos'))
    otros = [a for a in ARTICULOS if a['slug'] != slug][:3]
    return render_template('articulo.html',
        sports=SPORTS_CONFIG,
        art=art,
        otros=otros,
        current_sport=None,
    )


@app.route('/ads.txt')
def ads_txt():
    from flask import Response
    content = 'google.com, pub-2979871543216728, DIRECT, f08c47fec0942fa0\n'
    return Response(content, mimetype='text/plain')


@app.route('/google0f02660566dc23c6.html')
def google_verify():
    from flask import Response
    return Response('google-site-verification: google0f02660566dc23c6.html', mimetype='text/html')


@app.route('/robots.txt')
def robots_txt():
    from flask import Response
    content = (
        'User-agent: *\n'
        'Allow: /\n'
        'Disallow: /buscar\n\n'
        'Sitemap: https://deportes-mundo.onrender.com/sitemap.xml\n'
    )
    return Response(content, mimetype='text/plain')


@app.route('/sitemap.xml')
def sitemap_xml():
    from flask import Response
    BASE = 'https://deportes-mundo.onrender.com'
    urls = [
        ('/', '1.0', 'daily'),
        ('/futbol-latam', '0.9', 'daily'),
        ('/articulos', '0.7', 'weekly'),
    ]
    for key in SPORTS_CONFIG:
        urls.append((f'/deporte/{key}', '0.9', 'daily'))
    from articulos import ARTICULOS
    for art in ARTICULOS:
        urls.append((f'/articulo/{art["slug"]}', '0.6', 'monthly'))
    for sport_key, cfg in SPORTS_CONFIG.items():
        for p in cfg.get('historicos', []) + cfg.get('actuales', []):
            slug = urllib.parse.quote(p)
            urls.append((f'/jugador/{slug}', '0.5', 'weekly'))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, pri, freq in urls:
        lines.append(
            f'  <url><loc>{BASE}{path}</loc>'
            f'<priority>{pri}</priority>'
            f'<changefreq>{freq}</changefreq></url>'
        )
    lines.append('</urlset>')
    return Response('\n'.join(lines), mimetype='application/xml')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)