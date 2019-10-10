from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ccsbadmin .models import *
from django import forms

class GetIntouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ['name', 'email','message','subject',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['person_email','person_name','content','blog',]

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]
