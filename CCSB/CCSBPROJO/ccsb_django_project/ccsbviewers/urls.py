from django.conf.urls import url
from . import views

from django.urls import path
app_name = 'CCSB'
urlpatterns = [

    path('home/',views.home, name='home'),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('project/',views.project, name='project'),
    path('events/',views.events, name='events'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),

]