import os
import time
import json
import threading
import urllib.request
import urllib.parse
import feedparser
from flask import Flask, render_template, redirect, url_for, request, abort
from feeds import SPORTS_CONFIG, score_article

app = Flask(__name__)

_cache = {}
_cache_lock = threading.Lock()
CACHE_TTL = 30 * 60  # 30 minutos


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


@app.route('/jugador/<path:nombre>')
def jugador(nombre):
    player = get_player_wiki(nombre)

    sport_key = request.args.get('deporte', 'futbol')
    config = SPORTS_CONFIG.get(sport_key, SPORTS_CONFIG['futbol'])

    content_ideas = _content_ideas(player['name'], player['bio'])

    return render_template('jugador.html',
        sports=SPORTS_CONFIG,
        player=player,
        sport_key=sport_key,
        config=config,
        content_ideas=content_ideas,
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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
