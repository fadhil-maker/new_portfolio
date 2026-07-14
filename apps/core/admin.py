from django.contrib import admin
from .models import Profile, Education, Experience, Project, Skill, Certification

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'is_active')
    list_editable = ('is_active',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'grade', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'is_current', 'is_internship')
    search_fields = ('institution', 'degree')
    ordering = ('order',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'is_current', 'is_internship', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'is_current', 'is_internship')
    search_fields = ('company', 'role')
    ordering = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'card_color', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order', 'card_color')
    list_filter = ('is_active', 'is_featured')
    search_fields = ('title',)
    ordering = ('order',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'order')
    list_editable = ('is_active', 'order', 'category')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('title', 'issuer')
    ordering = ('order',)
