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

LATAM_CONFIG = {
    'conmebol': {
        'name': 'CONMEBOL',
        'color': '#003087',
        'ligas': {
            'copa-libertadores': {
                'name': 'Copa Libertadores',
                'flag': '🏆',
                'espn_slug': 'conmebol.libertadores',
                'feeds': ['https://news.google.com/rss/search?q=copa+libertadores&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Luiz Henrique', 'Germán Cano', 'Pablo Solari', 'Luciano Vietto'],
            },
            'copa-sudamericana': {
                'name': 'Copa Sudamericana',
                'flag': '🥈',
                'espn_slug': 'conmebol.sudamericana',
                'feeds': ['https://news.google.com/rss/search?q=copa+sudamericana&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Maxi Meza', 'Diego Churín', 'Matías Godoy'],
            },
            'argentina': {
                'name': 'Primera División Argentina',
                'flag': '🇦🇷',
                'espn_slug': 'arg.1',
                'feeds': ['https://news.google.com/rss/search?q=primera+division+argentina+boca+river&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Edinson Cavani', 'Miguel Borja', 'Lautaro Giannetti', 'Marcos Rojo'],
                'equipos': ['Boca Juniors', 'River Plate', 'Racing Club', 'Independiente', 'San Lorenzo', 'Estudiantes', 'Vélez Sársfield', 'Huracán'],
            },
            'brasil': {
                'name': 'Brasileirão Série A',
                'flag': '🇧🇷',
                'espn_slug': 'bra.1',
                'feeds': ['https://news.google.com/rss/search?q=brasileirao+serie+A+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Pedro', 'Yuri Alberto', 'Germán Cano', 'Hulk'],
                'equipos': ['Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Fluminense', 'São Paulo', 'Corinthians', 'Botafogo', 'Internacional'],
            },
            'colombia': {
                'name': 'Liga BetPlay Colombia',
                'flag': '🇨🇴',
                'espn_slug': 'col.1',
                'feeds': ['https://news.google.com/rss/search?q=liga+betplay+colombia+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Dayro Moreno', 'Christian Marrugo', 'Camilo Vargas', 'Jhon Duque'],
                'equipos': ['Atlético Nacional', 'Millonarios', 'América de Cali', 'Junior', 'Deportivo Cali', 'Santa Fe', 'Once Caldas', 'Deportes Tolima'],
            },
            'chile': {
                'name': 'Primera División Chile',
                'flag': '🇨🇱',
                'espn_slug': 'chi.1',
                'feeds': ['https://news.google.com/rss/search?q=primera+division+chile+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Darío Osorio', 'Lorenzo Reyes', 'Óscar Opazo'],
                'equipos': ['Colo-Colo', 'Universidad de Chile', 'Universidad Católica', 'Audax Italiano', 'Huachipato', 'Palestino'],
            },
            'peru': {
                'name': 'Liga 1 Perú',
                'flag': '🇵🇪',
                'espn_slug': 'per.1',
                'feeds': ['https://news.google.com/rss/search?q=liga+1+peru+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Hernán Barcos', 'Jairo Concha', 'Andy Polo'],
                'equipos': ['Universitario', 'Alianza Lima', 'Sporting Cristal', 'Melgar', 'César Vallejo', 'Binacional'],
            },
            'uruguay': {
                'name': 'Primera División Uruguay',
                'flag': '🇺🇾',
                'espn_slug': 'uru.1',
                'feeds': ['https://news.google.com/rss/search?q=primera+division+uruguay+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Darwin Núñez', 'Facundo Pellistri', 'Giorgian De Arrascaeta'],
                'equipos': ['Peñarol', 'Nacional', 'Defensor Sporting', 'Danubio', 'Liverpool Montevideo'],
            },
            'ecuador': {
                'name': 'LigaPro Ecuador',
                'flag': '🇪🇨',
                'espn_slug': 'ecu.1',
                'feeds': ['https://news.google.com/rss/search?q=ligapro+ecuador+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Enner Valencia', 'Michael Estrada', 'Ángel Mena'],
                'equipos': ['Barcelona SC', 'Liga de Quito', 'Emelec', 'El Nacional', 'Aucas', 'Independiente del Valle'],
            },
        },
    },
    'concacaf': {
        'name': 'CONCACAF',
        'color': '#c8102e',
        'ligas': {
            'champions-concacaf': {
                'name': 'CONCACAF Champions Cup',
                'flag': '🏆',
                'espn_slug': 'concacaf.champions',
                'feeds': ['https://news.google.com/rss/search?q=concacaf+champions+cup&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Memo Ochoa', 'Hirving Lozano', 'Efraín Álvarez'],
            },
            'liga-mx': {
                'name': 'Liga MX',
                'flag': '🇲🇽',
                'espn_slug': 'mex.1',
                'feeds': ['https://news.google.com/rss/search?q=liga+MX+mexico+futbol&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Hirving Lozano', 'Guillermo Ochoa', 'Julián Quiñones', 'Rogelio Funes Mori'],
                'equipos': ['Club América', 'Chivas Guadalajara', 'Cruz Azul', 'Pumas UNAM', 'Tigres UANL', 'Monterrey', 'Atlas', 'León'],
            },
            'costa-rica': {
                'name': 'Primera División Costa Rica',
                'flag': '🇨🇷',
                'espn_slug': 'crc.1',
                'feeds': ['https://news.google.com/rss/search?q=futbol+costa+rica+primera+division&hl=es-419&gl=US&ceid=US:es'],
                'top_jugadores': ['Keylor Navas', 'Bryan Ruiz', 'Joel Campbell'],
                'equipos': ['Deportivo Saprissa', 'Liga Deportiva Alajuelense', 'Herediano', 'Cartaginés'],
            },
        },
    },
}

MERCADO_VALOR = {
    'Lionel Messi': {'valor': '€35M', 'tm': 'lionel-messi'},
    'Vinicius Junior': {'valor': '€180M', 'tm': 'vinicius-junior'},
    'Erling Haaland': {'valor': '€200M', 'tm': 'erling-haaland'},
    'Kylian Mbappé': {'valor': '€180M', 'tm': 'kylian-mbappe'},
    'Pedri González': {'valor': '€100M', 'tm': 'pedri'},
    'Jude Bellingham': {'valor': '€180M', 'tm': 'jude-bellingham'},
    'Lamine Yamal': {'valor': '€180M', 'tm': 'lamine-yamal'},
    'Hirving Lozano': {'valor': '€18M', 'tm': 'hirving-lozano'},
    'Darwin Núñez': {'valor': '€70M', 'tm': 'darwin-nunez'},
    'Enner Valencia': {'valor': '€4M', 'tm': 'enner-valencia'},
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
