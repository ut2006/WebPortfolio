from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator  


# ─── Profile ─────────────────────────────────────────────────────────────────
class Profile(models.Model):
    user              = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name         = models.CharField(max_length=100)
    avatar            = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio               = models.TextField(blank=True, null=True)
    career_goal       = models.TextField(blank=True, null=True)
    core_values       = models.TextField(blank=True, null=True)
    achievements      = models.TextField(blank=True, null=True)
    achievement_image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    updated_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


# ─── Skill ───────────────────────────────────────────────────────────────────
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FE',   'Frontend'),
        ('BE',   'Backend'),
        ('SOFT', 'Soft Skill'),
    ]
    name     = models.CharField(max_length=50)
    level    = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.level}%)"


# ─── Project ─────────────────────────────────────────────────────────────────
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('React',  'React'),
        ('Js',     'JavaScript'),
        ('UI-UX',  'UI/UX'),
        ('DevOps', 'DevOps'),
    ]
    TYPE_CHOICES = [
        ('personal',  'Dự án cá nhân'),
        ('team',      'Dự án nhóm'),
        ('freelance', 'Dự án freelance'),
    ]
    title        = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    category     = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thumbnail    = models.ImageField(upload_to='projects/')
    tools_used   = models.CharField(max_length=200)
    year         = models.IntegerField()
    is_featured  = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ─── Blog ─────────────────────────────────────────────────────────────────────
class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('react',  'React'),
        ('js',     'JavaScript'),
        ('ui-ux',  'UI/UX'),
        ('devops', 'DevOps'),
    ]
    title       = models.CharField(max_length=200)
    summary     = models.TextField()
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thumbnail   = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ─── Contact ─────────────────────────────────────────────────────────────────
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20, blank=True, null=True)
    subject   = models.CharField(max_length=200)
    message   = models.TextField()
    sent_at   = models.DateTimeField(auto_now_add=True)
    is_read   = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
