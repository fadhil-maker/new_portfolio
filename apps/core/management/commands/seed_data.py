from django.core.management.base import BaseCommand
from apps.core.models import Profile, Education, Experience, Project, Skill, Certification


class Command(BaseCommand):
    help = 'Seeds the database with portfolio data for Muhammed Fadhil EH'

    def handle(self, *args, **options):
        self.stdout.write('Seeding portfolio data...')
        
        # Clear existing data
        Profile.objects.all().delete()
        Education.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Certification.objects.all().delete()
        
        # --- Profile ---
        Profile.objects.create(
            full_name='Muhammed Fadhil EH',
            title='FULL STACK',
            subtitle='DEVELOPER',
            tagline='In a world of digital noise, clarity is a story worth telling.',
            bio='I craft sleek, user-focused digital experiences with a passion for clean design and modern technology.\n\nWith a strong foundation in full-stack web development, I specialize in building fast, responsive, and elegant web applications.\n\nBeyond code, I\'m driven by creativity and a desire to build things that make an impact.',
            email='muhammedfadhileh@gmail.com',
            location='Kerala, India',
            github_url='https://github.com/fadhil-maker',
            instagram_url='https://www.instagram.com/_.fadhiluu._',
            portfolio_url='https://muhammedfadhil.vercel.app',
            order=1,
        )
        self.stdout.write(self.style.SUCCESS('  OK Profile created'))

        # --- Education ---
        Education.objects.create(
            institution='JCT College of Engineering and Technology',
            degree='B.E Computer Science and Engineering',
            field_of_study='Computer Science',
            start_date='2023',
            end_date='2026',
            grade='8.5/10',
            grade_label='CGPA',
            honours='',
            is_current=True,
            order=1,
        )
        self.stdout.write(self.style.SUCCESS('  OK Education seeded'))

        # --- Experience ---
        Experience.objects.create(
            company='ShanuDigiCore',
            company_url='',
            role='Digital Marketing Intern',
            start_date='Jun 2024',
            end_date='Aug 2024',
            description='Worked on digital marketing strategies, SEO optimization, and content creation for client brands.',
            technologies='SEO, Content Marketing, Social Media, Analytics',
            bullets=[
                'Managed social media campaigns across multiple platforms',
                'Performed SEO audits and implemented optimization strategies',
                'Created engaging content for brand visibility',
                'Analyzed campaign performance using analytics tools',
            ],
            is_current=False,
            order=1,
        )
        
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
        self.stdout.write(self.style.SUCCESS('  OK Experience seeded'))

        # --- Projects (NO FinEdge) ---
        Project.objects.create(
            title='Portfolio Website',
            subtitle='Personal Developer Portfolio with Modern UI',
            description='A fully responsive personal portfolio featuring a modern design with interactive elements. It showcases projects, skills, education, and experience with a clean, organized layout optimized for recruiters and collaborators.',
            technologies=[
                {'name': 'HTML', 'icon': 'html.svg'},
                {'name': 'CSS', 'icon': 'css.svg'},
                {'name': 'JavaScript', 'icon': 'javascript.svg'},
                {'name': 'Responsive UI', 'icon': 'responsive.svg'},
            ],
            github_url='https://github.com/fadhil-maker/portfolio',
            live_url='https://muhammedfadhil.vercel.app',
            card_color='#6366f1',
            number='01',
            is_featured=True,
            order=1,
        )

        Project.objects.create(
            title='ShanuDigiCore',
            subtitle='Digital Marketing & SEO Strategies',
            description='Led comprehensive digital marketing campaigns, performed in-depth SEO audits, and crafted engaging content that elevated brand visibility across multiple social platforms.',
            technologies=[
                {'name': 'SEO', 'icon': 'seo.svg'},
                {'name': 'Content Marketing', 'icon': 'content.svg'},
                {'name': 'Social Media', 'icon': 'social.svg'},
                {'name': 'Analytics', 'icon': 'analytics.svg'},
            ],
            live_url='',
            card_color='#10b981',
            number='02',
            is_featured=True,
            order=2,
        )
        self.stdout.write(self.style.SUCCESS('  OK Projects seeded'))

        # --- Skills ---
        skills_data = [
            ('Python', 'backend', 1, '<i class="devicon-python-plain text-2xl"></i>'),
            ('Django', 'backend', 2, '<i class="devicon-django-plain text-2xl"></i>'),
            ('JavaScript', 'frontend', 3, '<i class="devicon-javascript-plain text-2xl"></i>'),
            ('HTML5', 'frontend', 4, '<i class="devicon-html5-plain text-2xl"></i>'),
            ('CSS3', 'frontend', 5, '<i class="devicon-css3-plain text-2xl"></i>'),
            ('React', 'frontend', 6, '<i class="devicon-react-original text-2xl"></i>'),
            ('Node.js', 'backend', 7, '<i class="devicon-nodejs-plain-wordmark text-2xl"></i>'),
            ('Git', 'tools', 8, '<i class="devicon-git-plain text-2xl"></i>'),
            ('GitHub', 'tools', 9, '<i class="devicon-github-original text-2xl"></i>'),
            ('Linux', 'devops', 10, '<i class="devicon-linux-plain text-2xl"></i>'),
            ('Docker', 'devops', 11, '<i class="devicon-docker-plain text-2xl"></i>'),
            ('PostgreSQL', 'backend', 12, '<i class="devicon-postgresql-plain text-2xl"></i>'),
            ('Tailwind CSS', 'frontend', 13, '<i class="devicon-tailwindcss-original text-2xl"></i>'),
            ('Figma', 'tools', 15, '<i class="devicon-figma-plain text-2xl"></i>'),
        ]
        for name, category, order, icon in skills_data:
            Skill.objects.create(name=name, category=category, order=order, icon_svg=icon)
        self.stdout.write(self.style.SUCCESS(f'  OK {len(skills_data)} skills seeded'))

        # --- Certifications (placeholder) ---

        Certification.objects.create(
            title='Python-Django Certification',
            issuer='Kerala State Rutronix',
            credential_url='',
            order=1,
        )

        self.stdout.write(self.style.SUCCESS('  OK Certifications seeded'))

        self.stdout.write(self.style.SUCCESS('\nOK Database seeding complete!'))
