SPORTS_CONFIG = {
    'futbol': {
        'name': 'Fútbol',
        'emoji': '⚽',
        'color': '#00a651',
        'bg_dark': '#0a1f0f',
        'feeds': [
            'https://news.google.com/rss/search?q=futbol+mundial&hl=es-419&gl=US&ceid=US:es',
            'https://news.google.com/rss/search?q=liga+española+futbol&hl=es-419&gl=US&ceid=US:es',
            'https://news.google.com/rss/search?q=champions+league+futbol&hl=es-419&gl=US&ceid=US:es',
            'https://www.marca.com/rss/futbol.html',
            'https://as.com/rss/tags/futbol.xml',
        ],
        'historicos': [
            'Lionel Messi', 'Cristiano Ronaldo', 'Pelé', 'Diego Maradona',
            'Zinedine Zidane', 'Ronaldinho', 'Ronaldo Nazário', 'Johan Cruyff',
            'Franz Beckenbauer', 'Roberto Carlos',
        ],
        'actuales': [
            'Kylian Mbappé', 'Erling Haaland', 'Vinicius Junior',
            'Pedri González', 'Jude Bellingham', 'Rodri Hernández',
        ],
    },
    'baloncesto': {
        'name': 'Baloncesto',
        'emoji': '🏀',
        'color': '#e87722',
        'bg_dark': '#1f1005',
        'feeds': [
            'https://news.google.com/rss/search?q=NBA+baloncesto&hl=es-419&gl=US&ceid=US:es',
            'https://news.google.com/rss/search?q=baloncesto+mundial&hl=es-419&gl=US&ceid=US:es',
            'https://www.marca.com/rss/baloncesto.html',
        ],
        'historicos': [
            'Michael Jordan', 'LeBron James', 'Kobe Bryant', 'Magic Johnson',
            'Larry Bird', 'Shaquille O\'Neal', 'Bill Russell', 'Kareem Abdul-Jabbar',
            'Wilt Chamberlain', 'Oscar Robertson',
        ],
        'actuales': [
            'Giannis Antetokounmpo', 'Nikola Jokić', 'Stephen Curry',
            'Kevin Durant', 'Luka Dončić', 'Joel Embiid',
        ],
    },
    'tenis': {
        'name': 'Tenis',
        'emoji': '🎾',
        'color': '#c8a415',
        'bg_dark': '#1a1500',
        'feeds': [
            'https://news.google.com/rss/search?q=tenis+ATP+WTA&hl=es-419&gl=US&ceid=US:es',
            'https://news.google.com/rss/search?q=grand+slam+tenis&hl=es-419&gl=US&ceid=US:es',
            'https://www.marca.com/rss/tenis.html',
        ],
        'historicos': [
            'Roger Federer', 'Rafael Nadal', 'Pete Sampras', 'Novak Djokovic',
            'John McEnroe', 'Boris Becker', 'Stefan Edberg', 'Jimmy Connors',
            'Serena Williams', 'Steffi Graf',
        ],
        'actuales': [
            'Carlos Alcaraz', 'Jannik Sinner', 'Holger Rune',
            'Iga Świątek', 'Aryna Sabalenka', 'Coco Gauff',
        ],
    },
    'formula1': {
        'name': 'Fórmula 1',
        'emoji': '🏎️',
        'color': '#e10600',
        'bg_dark': '#1a0000',
        'feeds': [
            'https://news.google.com/rss/search?q=formula+1+F1&hl=es-419&gl=US&ceid=US:es',
            'https://news.google.com/rss/search?q=gran+premio+formula1&hl=es-419&gl=US&ceid=US:es',
            'https://www.marca.com/rss/motor/formula-1.html',
        ],
        'historicos': [
            'Michael Schumacher', 'Ayrton Senna', 'Lewis Hamilton',
            'Alain Prost', 'Niki Lauda', 'Jim Clark',
            'Jackie Stewart', 'Juan Manuel Fangio', 'Nigel Mansell', 'Nelson Piquet',
        ],
        'actuales': [
            'Max Verstappen', 'Charles Leclerc', 'Lando Norris',
            'Fernando Alonso', 'George Russell', 'Carlos Sainz',
        ],
    },
}

MONETIZABLE_KEYWORDS = {
    'alta': [
        'fichaje', 'transferencia', 'traspaso', 'contrato', 'millones',
        'récord', 'histórico', 'escándalo', 'polémico', 'polémica',
        'retiro', 'se retira', 'campeón', 'título mundial', 'sorpresa',
        'bomba', 'exclusiva', 'confirma', 'inesperado', 'impresionante',
    ],
    'media': [
        'lesión', 'lesionado', 'regresa', 'debut', 'primer', 'primera vez',
        'nuevo contrato', 'renovación', 'rumor', 'revelación', 'acuerdo',
    ],
}


def score_article(title, summary=''):
    text = (title + ' ' + summary).lower()
    score = 0
    score += sum(2 for kw in MONETIZABLE_KEYWORDS['alta'] if kw in text)
    score += sum(1 for kw in MONETIZABLE_KEYWORDS['media'] if kw in text)
    return score
