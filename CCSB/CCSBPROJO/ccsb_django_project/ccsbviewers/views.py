from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from ccsbadmin.models import *


def home(request):
    carousels = Carousel.objects.all()
    objectives = Objective.objects.all()
    experts = Expert.objects.all()
    today = datetime.date.today()
    events = Event.objects.filter(event_date__gt=today)[:3]
    contacts = Contact.objects.all()
    context = {
        'carousels':carousels,
        'objectives':objectives,
        'experts': experts,
        'events':events,
        'contacts':contacts
    }

    return render(request, 'normal/home/index.html', context)


def aboutUs(request):
    abouts = AboutUs.objects.all()
    experts = Expert.objects.all()

    context = {
        'abouts': abouts,
        'experts': experts,

    }
    return render(request, 'normal/aboutus/aboutus.html', context)


def project(request):
    projects = Project.objects.order_by("-created_at")

    context = {
        'projects':projects
    }
    return render(request, 'normal/projects/projects.html',context)


def events(request):
    today = datetime.date.today()
    events = Event.objects.filter(event_date__gt=today)[:3]

    context = {
        'events': events
    }
    return render(request, 'normal/events/events.html', context)


def blog(request):
    blogs = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(blogs, 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    context = {
        'blogs': blogs
    }
    return render(request, 'normal/blog/blog.html', context)


def contact(request):
    return render(request, 'normal/contact/contact.html')