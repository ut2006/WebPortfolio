from django.contrib import admin
from .models import Profile, Skill, Project, Blog, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'project_type', 'year', 'is_featured')
    list_filter = ('category', 'project_type', 'is_featured')
    search_fields = ('title', 'tools_used')
    list_editable = ('is_featured',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_featured')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'summary')
    list_editable = ('is_featured',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('full_name', 'email', 'subject')
    list_editable = ('is_read',)
    readonly_fields = ('full_name', 'email', 'phone', 'subject', 'message', 'sent_at')
