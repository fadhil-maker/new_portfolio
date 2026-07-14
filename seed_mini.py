import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from apps.core.models import Project

def seed():
    # Remove old placeholders
    Project.objects.filter(is_featured=False).delete()
    
    mini_projects = [
        {
            "title": "Aether",
            "slug": "aether",
            "description": "Ambient atmospheric telemetry simulator featuring Rain, Mist, Snow, and Thunder based on live weather data.",
            "technologies": ["Canvas API", "Open-Meteo API", "JavaScript"],
            "live_url": "/project/aether/",
            "card_color": "#13233c"
        },
        {
            "title": "Chroma Studio",
            "slug": "chroma",
            "description": "Interactive mechanical keyboard customizer managing hardware state logic arrays with dynamic audio feedback.",
            "technologies": ["Web Audio API", "DOM Manipulation", "CSS Grid"],
            "live_url": "/project/chroma/",
            "card_color": "#ff007f"
        },
        {
            "title": "Typing Defender",
            "slug": "typing-defender",
            "description": "Neon canvas shooter game running data destruction physics loops.",
            "technologies": ["Game Loop", "Canvas API", "Audio API"],
            "live_url": "/project/typing-defender/",
            "card_color": "#00e5ff"
        },
        {
            "title": "Gravity Golf",
            "slug": "gravity-golf",
            "description": "2D physics gravitational orbital launch calculator mapping trajectory curves to a singularity.",
            "technologies": ["Physics Engine", "Canvas API", "Mathematics"],
            "live_url": "/project/gravity-golf/",
            "card_color": "#ffaa00"
        },
        {
            "title": "Cyber Striker",
            "slug": "cyber-striker",
            "description": "Neon vertical space shooter featuring procedural enemy code grids, weapon upgrade drops, and chain explosions.",
            "technologies": ["Game Loop", "Canvas API", "Collision Detection"],
            "live_url": "/project/cyber-striker/",
            "card_color": "#ff4444"
        },
        {
            "title": "Glyph Matrix",
            "slug": "glyph-matrix",
            "description": "Image processing engine. Upload visual source materials to deconstruct graphics into active dot-matrix or text arrays.",
            "technologies": ["FileReader API", "Image Processing", "Canvas API"],
            "live_url": "/project/glyph-matrix/",
            "card_color": "#00ff66"
        }
    ]
    
    order = 10
    for p in mini_projects:
        proj = Project.objects.create(
            title=p['title'],
            description=p['description'],
            live_url=p['live_url'],
            card_color=p['card_color'],
            is_featured=False,
            order=order,
            technologies=[{"name": t} for t in p['technologies']]
        )
        order += 1
        
    print("Mini projects seeded successfully.")

if __name__ == "__main__":
    seed()
