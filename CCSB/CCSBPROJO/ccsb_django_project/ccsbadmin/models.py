from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
import datetime

# Create your models here.
class Admin(get_user_model()):
    profile_pic = models.ImageField(max_length=200, upload_to='adminprofile', null=True, blank=True)
    phone_no =  models.CharField(max_length=10, null=False, blank=False )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


class Carousel(models.Model):
    carousel_image = models.ImageField(upload_to='home_couresel',max_length=200,null=False, blank=False  ) #height_field=None, width_field=None,
    carousel_title = models.CharField(max_length=100, null=False, blank=False)
    carousel_description = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.carousel_image, self.carousel_title)

class Objective(models.Model):
    objective_title = models.CharField(max_length=150, null=False, blank=False)
    # objective_parent =
    objective_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.objective_title)

class Expert(models.Model):
    expert_image = models.ImageField(upload_to='experts', max_length=200, null=False, blank=False)  # height_field=None, width_field=None,
    expert_name= models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.expert_image, self.expert_name)


class Event(models.Model):
    events_image = models.ImageField(upload_to='events', max_length=200, null=False, blank=False)  # height_field=None, width_field=None,
    events_title = models.CharField(max_length=150, null=False, blank=False)
    events_description = models.TextField()
    event_date = models.DateTimeField(default=datetime.datetime.now())
    event_end_date = models.DateTimeField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.events_image, self.events_title)

    @property
    def upcomingEvents(self):
        today = datetime.date.today()
        events = Event.objects.filter(event_date__gt=today)
        if events is not  None:
            return events
        else:
            return False


class Newsletter(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.email)

class AboutUs(models.Model):
    about_image = models.ImageField(upload_to='aboutus', max_length=200, null=False, blank=False)  # height_field=None, width_field=None,
    about_title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.about_image, self.about_title)

class Contact(models.Model):
    email=models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s (%s)' % (self.email, self.phone_number, (self.address))

class Project(models.Model):
    project_image = models.ImageField(upload_to='project_image', max_length=200, null=False, blank=False)  # height_field=None, width_field=None,
    project_title = models.CharField(max_length=150, null=False, blank=False)
    project_description = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.project_title)

class Blog(models.Model):
    blog_image = models.ImageField(upload_to='events', max_length=200, null=True, blank=True)  # height_field=None, width_field=None,
    blog_title = models.CharField(max_length=150, null=False, blank=False)
    blog_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.blog_image, self.blog_title)

# class Chat(models.Model):
#     name = models.CharField(null=False, blank=False ,max_length=100)
#     phone_no = models.CharField(max_length=10, null=False, blank=False)
#     email = models.CharField(max_length=200, null=False, blank=False )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return '%s %s ' % (self.blog_image, self.blog_title)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=False,blank=False)
    person_name = models.CharField(max_length=100,null=True, blank=True)
    person_email = models.CharField(max_length=100,null=False, blank=False)
    content = models.TextField()

    COMMENTSSTATUS = {
        ('READ','Read'),
        ('UNREAD','Unread'),
        ('TRASH', 'Trash'),

    }
    status = models.CharField(choices=COMMENTSSTATUS, default='UNREAD', max_length=100,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.person_name)

class SocialMedia(models.Model):
    social_name = models.CharField(max_length=300, null=False, blank=False)
    social_url = models.URLField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.social_name, self.social_url)

class GetInTouch(models.Model):
     name = models.CharField(max_length=300, null=False, blank=False)
     email = models.CharField(max_length=300, null=False, blank=False)
     subject = models.CharField(max_length=300, null=True, blank=True)
     message = models.TextField()
     CHOICES= {
         ('READ', 'Read'),
         ('UNREAD', 'Unread'),
         ('TRASH', 'Trash'),
     }
     status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='UNREAD')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
         return '%s' % (self.name)