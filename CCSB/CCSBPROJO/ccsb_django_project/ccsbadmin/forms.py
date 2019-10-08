from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from django import forms

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields =('carousel_image','carousel_description','carousel_title',)

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['objective_title','objective_description',]

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ['expert_image','expert_name','description',]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title','blog_image','blog_description',]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['events_image', ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email','address','phone_number', ]

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['about_image','about_title','description',]


class AdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['profile_pic','username','first_name', 'last_name','phone_no','email','password1','password2',]

# class AdminImageForm(forms.ModelForm):
#     class Meta:
#         model = Admin
#         fields = []
















