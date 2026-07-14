from django.db import models


class BaseModel(models.Model):
    """Abstract base model with common fields for all portfolio models."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']


class Profile(BaseModel):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, help_text='e.g. FULL STACK')
    subtitle = models.CharField(max_length=200, help_text='e.g. DEVELOPER')
    tagline = models.TextField(blank=True, help_text='Hero section tagline')
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', max_length=500, blank=True, null=True)
    image_blend_amount = models.IntegerField(default=45, help_text='Percentage of picture covered by the bottom fade (e.g. 45)')
    resume_file = models.FileField(upload_to='resume/', max_length=500, blank=True, null=True, help_text='Upload your resume PDF')

    def __str__(self):
        return self.full_name


class Education(BaseModel):
    institution = models.CharField(max_length=300)
    degree = models.CharField(max_length=300)
    field_of_study = models.CharField(max_length=300, blank=True)
    start_date = models.CharField(max_length=20, help_text='e.g. 2023')
    end_date = models.CharField(max_length=20, help_text='e.g. 2026 or Present')
    grade = models.CharField(max_length=50, blank=True, help_text='e.g. 8.65/10')
    grade_label = models.CharField(max_length=100, blank=True, help_text='e.g. CGPA')
    honours = models.CharField(max_length=200, blank=True, help_text='e.g. Honours Student')
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)
    is_internship = models.BooleanField(default=False)
    certificate_file = models.FileField(upload_to='certificates/', max_length=500, blank=True, null=True, help_text='Upload internship certificate')

    def __str__(self):
        return f'{self.degree} - {self.institution}'


class Experience(BaseModel):
    company = models.CharField(max_length=300)
    company_url = models.URLField(blank=True)
    role = models.CharField(max_length=300)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20, default='Present')
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=500, blank=True, help_text='Comma-separated techs')
    bullets = models.JSONField(default=list, blank=True, help_text='List of bullet points')
    is_current = models.BooleanField(default=False)
    is_internship = models.BooleanField(default=False)
    certificate_file = models.FileField(upload_to='certificates/', max_length=500, blank=True, null=True, help_text='Upload internship certificate')

    def __str__(self):
        return f'{self.role} at {self.company}'


class Project(BaseModel):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500, blank=True)
    description = models.TextField()
    technologies = models.JSONField(
        default=list,
        help_text='List of dicts: [{"name": "Python", "icon": "python.svg"}]',
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', max_length=500, blank=True, null=True)
    video_url = models.URLField(blank=True)
    card_color = models.CharField(max_length=7, default='#6366f1', help_text='Hex color for card bg')
    number = models.CharField(max_length=5, default='01', help_text='Display number like 01, 02')
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Skill(BaseModel):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    icon_svg = models.TextField(blank=True, help_text='SVG markup or icon class')

    def __str__(self):
        return self.name


class Certification(BaseModel):
    title = models.CharField(max_length=300)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)
    credential_id = models.CharField(max_length=200, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.issuer}'
