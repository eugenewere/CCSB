from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from ccsbadmin.models import *
from ccsbviewers.forms import *


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
        'title':'Home',
        'events':events,
        'contacts':contacts
    }

    return render(request, 'normal/home/index.html', context)


def aboutUs(request):
    abouts = AboutUs.objects.all()
    experts = Expert.objects.all()

    context = {
        'abouts': abouts,
        'title': 'About Us',
        'experts': experts,

    }
    return render(request, 'normal/aboutus/aboutus.html', context)


def project(request):
    projects = Project.objects.order_by("-created_at")

    context = {
        'projects':projects,
        'title': 'Projects',

    }
    return render(request, 'normal/projects/projects.html',context)


def events(request):
    today = datetime.date.today()
    events = Event.objects.filter(event_date__gt=today).order_by("event_date__month").order_by("-event_date__day")

    page = request.GET.get('page', 1)

    paginator = Paginator(events, 6)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {
        'events': events,
        'title': 'Events',
    }
    return render(request, 'normal/events/events.html', context)


def blog(request):
    blogs = Blog.objects.all()
    comments = Comment.objects.order_by("-created_at")

    page = request.GET.get('page', 1)
    page2 = request.GET.get('page2', 1)

    paginator = Paginator(blogs, 1)
    paginator2 = Paginator(comments, 4)
    try:
        blogs = paginator.page(page)
        comments = paginator2.page(page2)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        comments = paginator2.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
        comments = paginator2.page(paginator2.num_pages)


    context = {
        'blogs': blogs,
        'comments':comments,
        'title': 'Blog',
    }
    return render(request, 'normal/blog/blog.html', context)


def contact(request):
    context ={
        'title': 'Contact',
    }
    return render(request, 'normal/contact/contact.html',context)


def getInTouch(request):
    if request.method == 'POST':
        form = GetIntouchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Comment Is Taken Successfuly')
        else:
            messages.error(request, 'Your Comment Not Taken Please Check Your Input Fields')
            return redirect('CCSB:contact')
    return redirect('CCSB:contact')


def addblogComment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Comment Is Taken Successfuly')
        else:
            messages.error(request, 'Your Comment Not Taken Please Check Your Input Fields')
            return redirect('CCSB:blog')
    return redirect('CCSB:blog')


def singleEvents(request, event_id):
    event = Event.objects.filter(id=event_id).first()

    context = {
        'event': event,
        'title': event.events_title,

    }
    return render(request, 'normal/events/singleevent.html',context)


def singleProject(request, project_id):
    project = Project.objects.filter(id=project_id).first()

    context = {
        'project': project,
        'title': project.project_title,

    }
    return render(request, 'normal/projects/singleproject.html', context)


def addNewsLetter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        # source = source.replace("____","/")
        # print(form)
        if form.is_valid():
            instance=form.save(commit=False)
            if Newsletter.objects.filter(email=instance.email):
                messages.error(request,'Sorry You Have Already Subscribed')
                return render(request, 'normal/newsletter/erroremailsubscription.html', {'email': instance.email})
            else:
                instance.save()
                messages.success(request, 'Thank you for submitting your email you will recieve emails frequently about this site')
                return render(request, 'normal/newsletter/successemailsubscription.html', {'email':instance.email})
        else:
            messages.error(request, 'Your Comment Not Taken Please Check Your Input Fields')
            return redirect("CCSB:home")
    return redirect("CCSB:home")