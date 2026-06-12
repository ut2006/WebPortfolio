from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Profile, Skill, Project, Blog
from .forms import ContactForm


# ─── Home  ─────────────────────────────────────────────────────────────
def home(request):
    profile  = Profile.objects.first()
    skills_fe = Skill.objects.filter(category='FE').order_by('-level')
    skills_be = Skill.objects.filter(category='BE').order_by('-level')
    skills_soft = Skill.objects.filter(category='SOFT')
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    featured_blogs    = Blog.objects.filter(is_featured=True)[:3]

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Tin nhắn đã được gửi! Tôi sẽ phản hồi trong vòng 24 giờ.')
            return redirect('home')

    context = {
        'profile': profile,
        'skills_fe': skills_fe,
        'skills_be': skills_be,
        'skills_soft': skills_soft,
        'featured_projects': featured_projects,
        'featured_blogs': featured_blogs,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)


# ─── Projects ─────────────────────────────────────────────────────────────────
def project_list(request):
    qs = Project.objects.all().order_by('-year')

    category = request.GET.get('category', '')
    ptype    = request.GET.get('type', '')
    q        = request.GET.get('q', '').strip()

    if category:
        qs = qs.filter(category=category)
    if ptype:
        qs = qs.filter(project_type=ptype)
    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(tools_used__icontains=q)

    paginator = Paginator(qs, 6)
    page_obj  = paginator.get_page(request.GET.get('page'))

    context = {
        'page_obj': page_obj,
        'category': category,
        'ptype': ptype,
        'q': q,
        'categories': Project.CATEGORY_CHOICES,
        'types': Project.TYPE_CHOICES,
        'total': qs.count(),
    }
    return render(request, 'portfolio/projects.html', context)



# ─── Blog ─────────────────────────────────────────────────────────────────────
def blog_list(request):
    qs = Blog.objects.all().order_by('-created_at')

    q = request.GET.get('q', '').strip()

    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(summary__icontains=q)

    paginator = Paginator(qs, 6)
    page_obj  = paginator.get_page(request.GET.get('page'))

    context = {
        'page_obj': page_obj,
        'q': q,
        'total': qs.count(),
    }
    return render(request, 'portfolio/blogs.html', context)

# ─── Contact ──────────────────────────────────────────────────────────────────
def contact(request):
    profile = Profile.objects.first()

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Tin nhắn đã được gửi! Tôi sẽ phản hồi trong vòng 24 giờ.')
            return redirect('contact')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)