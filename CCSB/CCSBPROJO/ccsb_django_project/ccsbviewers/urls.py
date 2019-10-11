from django.conf.urls import url
from . import views

from django.urls import path
app_name = 'CCSB'
urlpatterns = [

    path('home/',views.home, name='home'),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('project/',views.project, name='project'),
    path('singleProject/<int:project_id>',views.singleProject, name='singleProject'),
    path('events/',views.events, name='events'),
    path('singleEvents/<int:event_id>',views.singleEvents, name='singleEvents'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('getInTouch/',views.getInTouch, name='getInTouch'),
    path('addblogComment/', views.addblogComment, name='addblogComment'),
    path('addNewsLetter/', views.addNewsLetter, name='addNewsLetter'),


]