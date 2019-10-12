import json
from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import EmailMultiAlternatives, send_mail, send_mass_mail
from ccsb_django_project import settings
from ccsbadmin.models import *
from django.core import mail

# from django.contrib.auth import login as auth_login
# from django.http import HttpResponseRedirect
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.db.models import Q
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from django.utils.html import strip_tags
# from django.template.loader import get_template

# Create your views here.


# Create your views here.
@login_required()
def dashboard(request):
    experts_count = Expert.objects.all().count()
    today = date.today()
    comments = Comment.objects.order_by("-created_at")
    events_count =Event.objects.filter(event_date__gt=today).count()
    events = Event.objects.order_by("-event_date__date").order_by("-event_date__month")
    upcoming_event = Event.objects.filter(event_date__gte=today).first()
    project_count = Project.objects.all().count()
    comment_count = Comment.objects.all().count()
    get_intouch = GetInTouch.objects.all()
    emails = Newsletter.objects.all()
    user =request.user
    context ={
        'title':'Dashboard',
        'user': user,
        'experts_count':experts_count ,
        'events_count':events_count ,
        'project_count':project_count,
        'comment_count':comment_count,
        'events':events,
        'upcoming_event':upcoming_event,
        'get_intouch':get_intouch,
        'emails':emails,
        'comments':comments,

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
            #
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
            #
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
            #
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
            #
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
            #
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
            #
            form.save()
            messages.success(request, 'Blog Updated Successfuly')
        else:
            messages.error(request, 'Blog Not Updated')
            return redirect('CCSBADMIN:viewBlog')
    return redirect('CCSBADMIN:viewBlog')




def viewEvents(request):
    events = Event.objects.order_by('-created_at')
    context = {
        'title': 'Events',
        'events': events,

    }
    return render(request, 'event/events.html',context)





def viewCalendar(request):
    events = Event.objects.order_by('-created_at')
    all_events = Event.objects.all()
    get_event_types = Event.objects.only('events_title')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:
        event_arr = []
        if request.GET.get('events_title') == "all":
            all_events = EventForm.objects.all()
        else:
            all_events = EventForm.objects.filter(events_title__icontains=request.GET.get('events_title'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['events_title'] = i.event_name
            start_time = datetime.datetime.strptime(str(i.start_time.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_time = datetime.datetime.strptime(str(i.end_time.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['event_date'] = start_time
            event_sub_arr['event_end_date'] = end_time
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        'title': 'EventsCalendar',
        'events': events,

    }
    return render(request, 'event/calendar.html',context)
def homeCalendar(request):
    all_events = Event.objects.all()
    context = {
        "events":all_events,
    }
    return render(request, 'event/calendar.html', context)

def addCalendarEvent(request):
    if request.method == 'POST':
        event_date = request.POST['event_date']
        event_title = request.POST['events_title']
        event_end_date = request.POST['event_end_date']
        event_description = request.POST['events_description']
        evnt = Event.objects.create(
            event_date=event_date,
            events_title=event_title,
            event_end_date=event_end_date,
            events_description=event_description,
        )
        data = {}
        return JsonResponse(data)
    return redirect('TheAdmin:view-calenda')


def addEvents(request):
    if request.method == 'POST':
        event_date=request.POST['event_date']
        event_image=request.FILES['events_image']
        event_title=request.POST['events_title']
        event_end_date = request.POST['event_end_date']
        event_description=request.POST['events_description']
        evnt= Event.objects.create(
            event_date=event_date,
            events_image=event_image,
            events_title=event_title,
            event_end_date=event_end_date,
            events_description=event_description,
        )
        if evnt.id is not None:
            messages.success(request, 'Event Added Successfuly')
        else:
            messages.error(request, 'Event Not Added')
            return redirect('CCSBADMIN:viewEvents')
    return redirect('CCSBADMIN:viewEvents')

def editEvents(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    if request.method == 'POST':
        event_date=request.POST['event_date']
        event_image = request.FILES.get('events_image')
        event_title=request.POST['events_title']
        event_end_date=request.POST['event_end_date']
        event_description=request.POST['events_description']

        Event.objects.filter(id=event.id).update(
            event_date=event_date,
            events_image=event_image,
            event_end_date=event_end_date,
            events_title=event_title,
            events_description=event_description,
        )

        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():

            form.save()
            messages.success(request, 'Event Updated Successfuly')
        else:
            messages.error(request, 'Event Not Updated')
            return redirect('CCSBADMIN:viewEvents')

    return redirect('CCSBADMIN:viewEvents')


def deleteEvents(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    if event is not None:
        event.delete()
        messages.success(request, 'Event Deleted Successfuly')
        return redirect('CCSBADMIN:viewEvents')
    else:
        messages.error(request, 'Event Not Deleted')
        return redirect('CCSBADMIN:viewEvents')

def viewSingleEvents(request, event_id):
    event = Event.objects.filter(id=event_id).first()

    context = {
        'title':event.events_title,
        'event':event,
    }
    return render(request, 'event/singleevent.html',context)


def viewProjects(request):
    projects = Project.objects.order_by("-created_at")

    context = {
        'title': "Project",
        'projects': projects,
    }
    return render(request, 'projects/project.html', context)


def addProjects(request):
    if request.method == 'POST':
        date=request.POST['date']
        project_image=request.FILES['project_image']
        project_title=request.POST['project_title']
        project_description=request.POST['project_description']
        prjt= Project.objects.create(
            project_description=project_description,
            date=date,
            project_title=project_title,
            project_image=project_image,
        )
        if prjt.id is not None:
            messages.success(request, 'Project Added Successfuly')
        else:
            messages.error(request, 'Project Not Added')
            return redirect('CCSBADMIN:viewProjects')
    return redirect('CCSBADMIN:viewProjects')


def editProjects(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    if request.method == 'POST':
        date = request.POST['date']
        project_image = request.FILES.get('project_image')
        project_title = request.POST['project_title']
        project_description = request.POST['project_description']
        Project.objects.filter(id=int(project.id)).create(
            project_description=project_description,
            date=date,
            project_title=project_title,
            project_image=project_image,
        )
        messages.success(request, 'Project Updated Successfuly')
    return redirect('CCSBADMIN:viewProjects')


def deleteProjects(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    if project is not None:
        project.delete()
        messages.success(request, 'Project Deleted Successfuly')
        return redirect('CCSBADMIN:viewProjects')
    else:
        messages.error(request, 'Project Not Deleted')
        return redirect('CCSBADMIN:viewProjects')


def viewSingleProjects(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    context = {
        'title': project.project_title,
        'project': project,
    }
    return render(request,'projects/singleproject.html', context)


def viewContact(request):
    contacts = Contact.objects.order_by("created_at")
    context = {
        'title': 'Contacts',
        'contacts': contacts,
    }
    return render(request, 'contact/contact.html', context)


def addContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            #
            form.save()
            messages.success(request, 'Contact Added Successfuly')
        else:
            messages.error(request, 'Contact Not Added')
            return redirect('CCSBADMIN:viewContact')
    return redirect('CCSBADMIN:viewContact')


def deleteContact(request, contact_id):
    contact = Contact.objects.filter(id=contact_id).first()
    if contact is not None:
        contact.delete()
        messages.success(request, 'Contact Deleted Successfuly')
        return redirect('CCSBADMIN:viewContact')
    else:
        messages.error(request, 'Contact Not Deleted')
        return redirect('CCSBADMIN:viewContact')


def editContact(request, contact_id):
    contact = Contact.objects.filter(id=contact_id).first()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            #
            form.save()
            messages.success(request, 'Contact Updated Successfuly')
        else:
            messages.error(request, 'Contact Not Updated')
            return redirect('CCSBADMIN:viewContact')
    return redirect('CCSBADMIN:viewContact')


def aboutUs(request):
    aboutuss = AboutUs.objects.order_by("created_at")
    context = {
        'title': 'About Us',
        'aboutuss': aboutuss,
    }
    return render(request, 'aboutus/aboutus.html', context)


def addaboutUs(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)

        if form.is_valid():
            #
            form.save()
            messages.success(request, 'Your Story Added Successfuly')
        else:
            messages.error(request, 'Your Story Not Added')
            return redirect('CCSBADMIN:aboutUs')
    return redirect('CCSBADMIN:aboutUs')


def deleteaboutUs(request, aboutus_id):
    aboutus = AboutUs.objects.filter(id=aboutus_id).first()
    if aboutus is not None:
        aboutus.delete()
        messages.success(request, 'Your story Deleted Successfuly')
        return redirect('CCSBADMIN:aboutUs')
    else:
        messages.error(request, 'Your story Not Deleted')
        return redirect('CCSBADMIN:aboutUs')


def editaboutUs(request, aboutus_id):
    aboutus = AboutUs.objects.filter(id=aboutus_id).first()
    if request.method == 'POST':
        form = AboutUsForm(request.POST,request.FILES, instance=aboutus )

        if form.is_valid():
            #
            form.save()
            messages.success(request, 'Your Story Updated Successfuly')
        else:
            messages.error(request, 'Your Story Not Updated')
            return redirect('CCSBADMIN:aboutUs')
    return redirect('CCSBADMIN:aboutUs')


def singleaboutUs(request, aboutus_id):
    aboutus = AboutUs.objects.filter(id=aboutus_id).first()
    context = {
        'title': aboutus.about_title,
        'aboutus': aboutus,
    }
    return render(request, 'aboutus/singleaboutus.html', context)






def register(request):
    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES)


        if form.is_valid() :
            # user = form.save(commit=False)
            # user.profile_pic = request.FILES.get('profile_pic')
            form.save()
            messages.success(request, 'Registered Successfully Now Log In')
            return redirect('CCSBADMIN:login')
        else:
            form = AdminForm()

            messages.error(request, 'Registration Error')
            return render(request, "register/register.html", {'form': form})
    context = {

    }

    return render(request, 'register/register.html',context)


def adminlogin(request):
    messages = []
    admins = Admin.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('CCSBADMIN:dashboard')
            else:
                messages.append('Your account has been activated!')
                return render(request, 'register/login.html', {'success': messages})
        else:
            messages.append('Invalid login credentials!')
            return render(request, 'register/login.html', {'errors': messages})
    return render(request, "register/login.html", {'admins':admins})


def adminlogout(request):
    logout(request)
    return redirect('CCSBADMIN:login')




def comment(request):
    comments = Comment.objects.all()

    context = {
        'title':'comment',
        'comments':comments
    }
    return render(request,'comments/comment.html', context)


def singleComment(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if comment is not None:
        Comment.objects.filter(id=int(comment.id)).update(
            status='READ'
        )
    context = {
        'title':comment.person_name,
        'comment': comment
    }
    return render(request,'comments/singlecomment.html', context)


def singleCommentDelete(request,comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if comment is not None:
        comment.delete()
        messages.success(request,'Comment Deleted Succesfully')
        return redirect("CCSBADMIN:comment")
    return redirect("CCSBADMIN:comment")


def getintouch(request):
    getintouchs = GetInTouch.objects.all()

    context = {
        'title': 'getintouch',
        'getintouchs': getintouchs
    }
    return render(request, 'getintouch/getintouch.html',context)


def deletegetintouch(request, getintouch_id):
    getintouch = GetInTouch.objects.filter(id=getintouch_id).first()
    if getintouch is not None:
        getintouch.delete()
        messages.success(request, getintouch.name+'Deleted Succesfully')
        return redirect("CCSBADMIN:getintouch")
    return redirect("CCSBADMIN:getintouch")


def singlegetintouch(request,getintouch_id):
    getintouch = GetInTouch.objects.filter(id=getintouch_id).first()
    if getintouch is not None:
        GetInTouch.objects.filter(id=int(getintouch.id)).update(
            status='READ'
        )
    context = {
        'title': getintouch.name,
        'getintouch': getintouch
    }
    return render(request, 'getintouch/singlegetintouch.html', context)

def newsLetter(request):
    emails = Newsletter.objects.all()
    newslettermessages = NewsletterMessage.objects.all()
    context = {
        'title':'NewsLetter',
        'emails':emails,
        'newslettermessages':newslettermessages,
    }
    return render(request,'newsletter/newsletter.html', context)


def sendEmails(request):
    if request.method == "POST":
        body = request.POST['message']
        subject = request.POST['subject']
        emails = Newsletter.objects.all()

        NewsletterMessage.objects.create(
            subject=subject,
            message=body,
            email_count=emails.count()
        )

        messages.success(request, 'Messages Saved')
        for email in emails:
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email.email,]
            send_mail(
                subject=subject,
                message=body,
                from_email=email_from,
                recipient_list=recipient_list
            )
        messages.success(request, 'Emails sent')
        return redirect('CCSBADMIN:newsLetter')
    return redirect('CCSBADMIN:newsLetter')


def singlenewsLetter(request, newslettermessage_id):
    newsmessge = NewsletterMessage.objects.filter(id=newslettermessage_id).first()
    context = {
        'title':newsmessge.subject,
        'newsmessge':newsmessge,
    }

    return render(request, 'newsletter/singlenewsletter.html', context)


def account(request):
    user_id=request.user.id
    admin = Admin.objects.filter(user_ptr_id=user_id).first()

    context = {
        'title': "user account",
        'admin': admin,
    }
    return render(request, 'account/account.html', context)


def updateaccount(request):
    user_id = request.user.id
    admin = Admin.objects.filter(user_ptr_id=user_id).first()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        # image= request.FILES.get('image', None)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_no']
        if admin is not None:
            Admin.objects.filter(user_ptr_id=admin.id).update(
                # profile_pic=image,
                phone_no=phone_number,
            )
            User.objects.filter(pk = request.user.id).update(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )

            messages.success(request, 'Updated Successfully')
        return redirect('CCSBADMIN:account')
    return redirect('CCSBADMIN:account')


def updateaccountprofilepic(request):
    user_id = request.user.id
    admin = Admin.objects.filter(user_ptr_id=user_id).first()
    if request.method == "POST":
        image = request.FILES['profile_pic']
        form = AdminForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
            form.save(commit=False)
            form.profile_pic = image
            form.save()
            messages.success(request, 'Updated Successfully')
            return redirect("CCSBADMIN:updateaccountprofilepic")

    context = {
        'title': "user account",
        'admin': admin,
    }
    return render(request, 'account/editpicture.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('CCSBADMIN:account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'account/editpassword.html', {
        'form': form
    })