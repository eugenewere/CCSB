import statistics

from django import template
from django.shortcuts import render_to_response
from django.views import View

from ccsbadmin.models import *

register = template.Library()

@register.filter(name='contacts')
def user(request):
    contacts = Contact.objects.all()
    if contacts is not None:
        return contacts
    return False