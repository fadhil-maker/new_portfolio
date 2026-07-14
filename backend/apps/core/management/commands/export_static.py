import os
import shutil
from django.core.management.base import BaseCommand
from django.test import Client
from django.conf import settings

class Command(BaseCommand):
    help = 'Exports the Django site to static HTML files for GitHub Pages'

    def handle(self, *args, **kwargs):
        out_dir = os.path.join(settings.BASE_DIR, 'out')
        
        # 1. Clean output directory
        if os.path.exists(out_dir):
            shutil.rmtree(out_dir)
        os.makedirs(out_dir)
        self.stdout.write(self.style.WARNING(f'Cleaned {out_dir}'))
        
        # 2. Fetch the homepage using Django's test client
        client = Client()
        response = client.get('/')
        
        if response.status_code == 200:
            html_content = response.content.decode('utf-8')
            
            # 3. Write index.html
            index_path = os.path.join(out_dir, 'index.html')
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            self.stdout.write(self.style.SUCCESS('Successfully exported index.html'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch homepage. Status code: {response.status_code}'))
            return
            
        # 4. Copy Static files
        static_src = os.path.join(settings.BASE_DIR, 'staticfiles')
        if not os.path.exists(static_src):
            # Fallback to static if collectstatic hasn't been run
            static_src = os.path.join(settings.BASE_DIR, 'static')
            
        static_dst = os.path.join(out_dir, 'static')
        if os.path.exists(static_src):
            shutil.copytree(static_src, static_dst)
            self.stdout.write(self.style.SUCCESS(f'Copied static files from {static_src}'))
            
        # 5. Copy Media files
        media_src = os.path.join(settings.BASE_DIR, 'media')
        media_dst = os.path.join(out_dir, 'media')
        if os.path.exists(media_src):
            shutil.copytree(media_src, media_dst)
            self.stdout.write(self.style.SUCCESS('Copied media files'))
            
        self.stdout.write(self.style.SUCCESS('\nStatic export complete! You can now deploy the "out" folder to GitHub Pages.'))
