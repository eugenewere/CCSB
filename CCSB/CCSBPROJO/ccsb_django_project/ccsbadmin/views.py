from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def dashboard(request):

    context ={
        'title':'Dashboard'
    }

    return render(request, 'aahome/index.html', context)

def viewCarousels(request):
    carousels = Carousel.objects.order_by('-created_at')

    context ={
        'title':'HomePageCarousel',
        'carousels': carousels,
    }

    return render(request, 'carousels/carousel.html', context)

def addCarousels(request):
    if request.method == 'POST':
        form = CarouselForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'Carousel Added Successfuly')
        else:
            messages.error(request, 'Carousel Not Added')
            return redirect('CCSBADMIN:viewCarousels')
    return redirect('CCSBADMIN:viewCarousels')

def deleteCarousels(request, carousel_id):
    carousel = Carousel.objects.filter(id=carousel_id).first()
    if carousel is not None:
        carousel.delete()
        messages.success(request, 'Carousel Deleted Successfuly')
        return redirect('CCSBADMIN:viewCarousels')
    else:
        messages.error(request, 'Carousel Not Deleted')
        return redirect('CCSBADMIN:viewCarousels')

def editCarousels(request, carousel_id):
    carousel = Carousel.objects.filter(id=carousel_id).first()
    if request.method == 'POST':
        form = CarouselForm(request.POST, request.FILES, instance=carousel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carousel Updated Successfuly')
        else:
            messages.error(request, 'Carousel Not Updated')
            return redirect('CCSBADMIN:viewCarousels')
    return redirect('CCSBADMIN:viewCarousels')


def viewObjectives(request):
    objectives = Objective.objects.order_by("-created_at")

    context ={
        'title':'Objectives',
        'objectives': objectives,

    }

    return render(request, 'objectives/ojectives.html', context)

def addObjectives(request):
    if request.method == 'POST':
        form = ObjectiveForm(request.POST)
        print(form)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'Objectives  Added Successfuly')
        else:
            messages.error(request, 'Objectives Not Added')
            return redirect('CCSBADMIN:viewObjectives')
    return redirect('CCSBADMIN:viewObjectives')

def specificObjectives(request, objective_id):
    objective = Objective.objects.filter(id=objective_id).first()

    context ={
        'title':objective.objective_title,
        'objective': objective,

    }
    return render(request, 'objectives/viewobjective.html', context)

def deleteObjectives(request, objective_id):
    objective = Objective.objects.filter(id=objective_id).first()

    if objective is not None:
        objective.delete()
        messages.success(request, 'Objective Deleted Successfuly')
        return redirect('CCSBADMIN:viewObjectives')
    else:
        messages.error(request, 'Objective Not Deleted')
        return redirect('CCSBADMIN:viewObjectives')

def updateObjectives(request, objective_id):
    objective = Objective.objects.filter(id=objective_id).first()

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objective Updated Successfuly')
        else:
            messages.error(request, 'Objective Not Updated')
            return redirect('CCSBADMIN:viewObjectives')
    return redirect('CCSBADMIN:viewObjectives')





def viewExpert(request):
    experts = Expert.objects.order_by("-created_at")

    context = {
        'title': 'Experts',
        'experts': experts,

    }

    return render(request, 'team/viewteam.html', context)

def addExpert(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'Expert Added Successfuly')
        else:
            messages.error(request, 'Expert Not Added')
            return redirect('CCSBADMIN:viewExpert')
    return redirect('CCSBADMIN:viewExpert')

def deleteExpert(request, expert_id):
    expert = Expert.objects.filter(id=expert_id).first()

    if expert is not None:
        expert.delete()
        messages.success(request, 'Expert Deleted Successfuly')
        return redirect('CCSBADMIN:viewExpert')
    else:
        messages.error(request, 'Expert Not Deleted')
        return redirect('CCSBADMIN:viewExpert')

def editExpert(request, expert_id):
    expert = Expert.objects.filter(id=expert_id).first()
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES, instance=expert)
        print(form)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'Expert Updated Successfuly')
        else:
            messages.error(request, 'Expert Not Updated')
            return redirect('CCSBADMIN:viewExpert')
    return redirect('CCSBADMIN:viewExpert')






def viewBlog(request):
    blogs = Blog.objects.order_by("-created_at")

    context = {
        'title': 'Blogs',
        'blogs': blogs,

    }

    return render(request, 'blog/blog.html', context)

def addBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'Blog Added Successfuly')
        else:
            messages.error(request, 'Blog Not Added')
            return redirect('CCSBADMIN:viewBlog')
    return redirect('CCSBADMIN:viewBlog')

def viewSingleBlog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()

    context ={
        'title':blog.blog_title,
        'blog': blog,

    }
    return render(request, 'blog/singleblog.html', context)

def deleteBlog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    if blog is not None:
        blog.delete()
        messages.success(request, 'Blog Deleted Successfuly')
        return redirect('CCSBADMIN:viewBlog')
    else:
        messages.error(request, 'Blog Not Deleted')
        return redirect('CCSBADMIN:viewBlog')

def updateBlog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        print(form)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'Blog Updated Successfuly')
        else:
            messages.error(request, 'Blog Not Updated')
            return redirect('CCSBADMIN:viewBlog')
    return redirect('CCSBADMIN:viewBlog')












