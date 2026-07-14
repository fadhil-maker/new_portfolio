from django.shortcuts import render, get_object_or_404

from .models import Profile, Education, Experience, Project, Skill, Certification


def portfolio_view(request):
    """Main portfolio page view."""
    profile = Profile.objects.filter(is_active=True).first()
    education = Education.objects.filter(is_active=True).order_by('order')
    experience = Experience.objects.filter(is_active=True, is_internship=False).order_by('order')
    internships = Experience.objects.filter(is_active=True, is_internship=True).order_by('order')
    projects = Project.objects.filter(is_active=True, is_featured=True).order_by('order')
    mini_projects = Project.objects.filter(is_active=True, is_featured=False).order_by('order')
    certifications = Certification.objects.filter(is_active=True).order_by('order')
    
    # Group skills by category
    skills = Skill.objects.filter(is_active=True).order_by('order')
    skills_grouped = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_grouped:
            skills_grouped[category] = []
        skills_grouped[category].append(skill)
    
    context = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'internships': internships,
        'projects': projects,
        'mini_projects': mini_projects,
        'skills': skills,
        'skills_grouped': skills_grouped,
        'certifications': certifications,
    }
    return render(request, 'core/index.html', context)


def mini_project_view(request, slug):
    project = get_object_or_404(Project, live_url=f"/project/{slug}/")
    context = {
        'project': project,
    }
    return render(request, f'core/mini_projects/{slug}.html', context)

