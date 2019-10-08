import statistics

from django import template
from django.shortcuts import render_to_response
from django.views import View

from ccsbadmin.models import *

register = template.Library()

@register.filter(name='admin')
def user(request):
    admin = Admin.objects.filter(id=request.user.id).first()
    if admin is not None:
        return admin.profile_pic
    return False

@register.filter(name='contacts')
def contacts(request):
    contact = Contact.objects.all()
    if contact is not None:
        return contact
    return False