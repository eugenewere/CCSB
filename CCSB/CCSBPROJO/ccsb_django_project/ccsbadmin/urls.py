from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'CCSBADMIN'
urlpatterns =[
    path('dashboard/', views.dashboard, name='dashboard'),

    path('carousels/', views.viewCarousels, name='viewCarousels'),
    path('addcarousels/', views.addCarousels, name='addCarousels'),
    path('deletecarousels/<int:carousel_id>', views.deleteCarousels, name='deleteCarousels'),
    path('editcarousels/<int:carousel_id>', views.editCarousels, name='editCarousels'),

    path('objectives/', views.viewObjectives, name='viewObjectives'),
    path('specificobjectives/<int:objective_id>', views.specificObjectives, name='specificObjectives'),
    path('deleteobjectives/<int:objective_id>', views.deleteObjectives, name='deleteObjectives'),
    path('updateobjectives/<int:objective_id>', views.updateObjectives, name='updateObjectives'),
    path('addobjectives/', views.addObjectives, name='addObjectives'),

    path('viewexperts/', views.viewExpert, name='viewExpert'),
    path('addexperts/', views.addExpert, name='addExpert'),
    path('deleteexperts/<int:expert_id>', views.deleteExpert, name='deleteExpert'),
    path('editexperts/<int:expert_id>', views.editExpert, name='editExpert'),

    path('blog/',views.viewBlog, name='viewBlog'),
    path('addblog/',views.addBlog, name='addBlog'),
    path('viewSingleblog/<int:blog_id>',views.viewSingleBlog, name='viewSingleBlog'),
    path('deleteblog/<int:blog_id>',views.deleteBlog, name='deleteBlog'),
    path('updateblog/<int:blog_id>',views.updateBlog, name='updateBlog'),

]