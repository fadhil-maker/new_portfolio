import os
import shutil
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Project, Education

# 1. Update Projects with images
img1_src = r'C:\Users\vavac\.gemini\antigravity\brain\84792804-2873-4737-9d29-7ea6354610d6\portfolio_ui_1783190803819.png'
img2_src = r'C:\Users\vavac\.gemini\antigravity\brain\84792804-2873-4737-9d29-7ea6354610d6\analytics_dash_1783190813710.png'
dest_dir = r'C:\Users\vavac\OneDrive\Desktop\port\media\projects'
os.makedirs(dest_dir, exist_ok=True)

img1_dest = os.path.join(dest_dir, 'portfolio.png')
img2_dest = os.path.join(dest_dir, 'analytics.png')

shutil.copy2(img1_src, img1_dest)
shutil.copy2(img2_src, img2_dest)

p1 = Project.objects.filter(title__icontains='Portfolio').first()
if p1:
    p1.image = 'projects/portfolio.png'
    p1.save()

p2 = Project.objects.filter(title__icontains='Shanu').first()
if p2:
    p2.image = 'projects/analytics.png'
    p2.save()

# 2. Update Education
Education.objects.all().delete()

Education.objects.create(
    institution='JCT College of Engineering and Technology',
    degree='B.Tech in Computer Science with Business Systems',
    field_of_study='Computer Science',
    start_date='2023',
    end_date='2027',
    grade='Pursuing',
    grade_label='Status',
    is_current=True,
    order=1,
)

Education.objects.create(
    institution='St. Aloysius Higher Secondary School, Elthuruth',
    degree='Electronic Science',
    field_of_study='Science',
    start_date='2021',
    end_date='2023',
    grade='90%',
    grade_label='Marks',
    is_current=False,
    order=2,
)

Education.objects.create(
    institution='Lourde Matha EMHSS, Cherpu',
    degree='SSLC',
    field_of_study='General',
    start_date='2020',
    end_date='2021',
    grade='95%',
    grade_label='Marks',
    is_current=False,
    order=3,
)

print("Database successfully updated with new education and project images.")
