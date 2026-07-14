import os

def update_models():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\apps\core\models.py"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Experience
    if "is_internship" not in content:
        content = content.replace(
            "is_current = models.BooleanField(default=False)",
            "is_current = models.BooleanField(default=False)\n    is_internship = models.BooleanField(default=False)\n    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True, help_text='Upload internship certificate')"
        )

    # Update Certification
    if "certificate_file = models.FileField" not in content.split("class Certification")[1]:
        content = content.replace(
            "credential_id = models.CharField(max_length=200, blank=True)",
            "credential_id = models.CharField(max_length=200, blank=True)\n    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)"
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def update_admin():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\apps\core\admin.py"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "'is_internship'" not in content:
        content = content.replace(
            "list_display = ('role', 'company', 'start_date', 'end_date', 'is_current', 'is_active', 'order')",
            "list_display = ('role', 'company', 'start_date', 'end_date', 'is_current', 'is_internship', 'is_active', 'order')"
        )
        content = content.replace(
            "list_filter = ('is_active', 'is_current')",
            "list_filter = ('is_active', 'is_current', 'is_internship')"
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def update_seed_data():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\apps\core\management\commands\seed_data.py"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Experience seeding to include Cyborg AI
    if "Cyborg AI Gen Automation" not in content:
        new_exp = """
        Experience.objects.create(
            company='Cyborg AI Gen Automation',
            company_url='',
            role='Data Science Intern',
            start_date='2023',
            end_date='2023',
            description='Implementing predictive modeling and deep data analysis on real-world datasets.',
            technologies='Data Science, Predictive Modeling, Python',
            bullets=[
                'Developed machine learning models for predictive analysis',
                'Analyzed complex datasets to extract actionable insights',
            ],
            is_current=False,
            is_internship=True,
            order=1,
        )
"""
        content = content.replace("self.stdout.write(self.style.SUCCESS('  OK Experience seeded'))", new_exp + "self.stdout.write(self.style.SUCCESS('  OK Experience seeded'))")

    # Update Certifications seeding to include Rutronix
    if "Kerala State Rutronix" not in content:
        new_cert = """
        Certification.objects.create(
            title='Python-Django Certification',
            issuer='Kerala State Rutronix',
            credential_url='',
            order=1,
        )
"""
        # Remove placeholder certification
        content = content.replace("""        Certification.objects.create(
            title='Python for Everybody',
            issuer='Coursera',
            credential_url='',
            order=1,
        )""", new_cert)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def update_views():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\apps\core\views.py"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "experience = Experience.objects.filter(is_active=True, is_internship=False).order_by('order')" not in content:
        content = content.replace(
            "experience = Experience.objects.filter(is_active=True).order_by('order')",
            "experience = Experience.objects.filter(is_active=True, is_internship=False).order_by('order')\n    internships = Experience.objects.filter(is_active=True, is_internship=True).order_by('order')"
        )
        content = content.replace(
            "'experience': experience,",
            "'experience': experience,\n        'internships': internships,"
        )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_models()
    update_admin()
    update_seed_data()
    update_views()
