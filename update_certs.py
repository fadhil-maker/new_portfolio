import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Experience, Certification

# Update Cyborg AI
cyborg = Experience.objects.filter(company='Cyborg AI Gen Automation').first()
if cyborg:
    cyborg.certificate_file = 'certificates/data_science_cert.jpg'
    cyborg.save()
    print("Updated Cyborg AI Gen Automation")

# Update Rutronix
rutronix = Certification.objects.filter(issuer='Kerala State Rutronix').first()
if rutronix:
    rutronix.certificate_file = 'certificates/django_cert.jpg'
    rutronix.save()
    print("Updated Rutronix Certification")
