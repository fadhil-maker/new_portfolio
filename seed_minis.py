import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Project

mini_projects = [
    {
        'title': 'Chroma',
        'subtitle': 'Interactive Hardware Matrix',
        'description': 'Hardware logic puzzle where you tap keys to inject custom hex codes into a grid.',
        'live_url': '/mini/chroma/',
        'number': '03',
        'card_color': '#3b82f6',
    },
    {
        'title': 'Cyber Striker',
        'subtitle': 'Canvas Space Shooter',
        'description': 'Arcade style shooter where you obliterate oncoming corrupted code cores and gather node upgrades.',
        'live_url': '/mini/cyber-striker/',
        'number': '04',
        'card_color': '#ef4444',
    },
    {
        'title': 'Glyph Matrix',
        'subtitle': 'Logic Puzzle',
        'description': 'A beautiful puzzle game where you connect matching nodes without crossing their data streams.',
        'live_url': '/mini/glyph-matrix/',
        'number': '05',
        'card_color': '#00e5ff',
    },
    {
        'title': 'Typing Defender',
        'subtitle': 'Keyboard Defense',
        'description': 'Rapid-fire typing game. Defend the core by typing the incoming words before they breach the firewall.',
        'live_url': '/mini/typing-defender/',
        'number': '06',
        'card_color': '#ff007f',
    }
]

for idx, p in enumerate(mini_projects, start=3):
    Project.objects.create(
        title=p['title'],
        subtitle=p['subtitle'],
        description=p['description'],
        live_url=p['live_url'],
        number=p['number'],
        card_color=p['card_color'],
        is_featured=False,
        order=idx
    )

print("Added the 4 remaining Mini Projects to the database!")
