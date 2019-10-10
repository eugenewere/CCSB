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

@register.filter(name='comments')
def contacts(request):
    comments = Comment.objects.filter(status="UNREAD").order_by("-created_at")
    if comments is not None:
        return comments
    return False

@register.filter(name='get_intouch')
def contacts(request):
    getintouchs = GetInTouch.objects.filter(status="UNREAD").order_by("-created_at")
    if getintouchs  is not None:
        return getintouchs
    return False

@register.filter(name='comment_unread_count')
def contacts(request):
    unread_comments = Comment.objects.filter(status="UNREAD").count()
    if unread_comments is not None:
        return unread_comments
    return False

@register.filter(name='getintouch_unread_count')
def contacts(request):
    getintouch_unread_count = GetInTouch.objects.filter(status="UNREAD").count()
    if getintouch_unread_count is not None:
        return getintouch_unread_count
    return False



















