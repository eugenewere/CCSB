from django.conf.urls import url
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


app_name = 'CCSBADMIN'
urlpatterns =[
    path('dashboard/', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),
    path('login/', views.adminlogin, name='login'),
    path('logout/', views.adminlogout, name='logout'),

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

    path('viewEvents/', views.viewEvents, name='viewEvents'),
         path('viewCalendar/', views.viewCalendar, name='viewCalendar'),
         path('viewhomeCalenda', views.homeCalendar, name='view-calenda'),
         path('addevent', views.addCalendarEvent, name='add-Event'),
    path('addEvents/', views.addEvents, name='addEvents'),
    path('editEvents/<int:event_id>', views.editEvents, name='editEvents'),
    path('viewSingleEvents/<int:event_id>', views.viewSingleEvents, name='viewSingleEvents'),
    path('deleteEvents/<int:event_id>', views.deleteEvents, name='deleteEvents'),

    path('viewProjects/', views.viewProjects, name='viewProjects'),
    path('addProjects/', views.addProjects, name='addProjects'),
    path('editProjects/<int:project_id>/', views.editProjects, name='editProjects'),
    path('deleteProjects/<int:project_id>/', views.deleteProjects, name='deleteProjects'),
    path('viewSingleProjects/<int:project_id>/', views.viewSingleProjects, name='viewSingleProjects'),

    path('contacts/', views.viewContact, name='viewContact'),
    path('addcontacts/', views.addContact, name='addContact'),
    path('deletecontacts/<int:contact_id>', views.deleteContact, name='deleteContact'),
    path('editcontacts/<int:contact_id>', views.editContact, name='editContact'),

    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('addaboutUs/',views.addaboutUs, name='addaboutUs'),
    path('deleteaboutUs/<int:aboutus_id>',views.deleteaboutUs, name='deleteaboutUs'),
    path('editaboutUs/<int:aboutus_id>',views.editaboutUs, name='editaboutUs'),
    path('singleaboutUs/<int:aboutus_id>',views.singleaboutUs, name='singleaboutUs'),



    path('comment/', views.comment, name='comment'),
    path('singlecomment/<int:comment_id>', views.singleComment, name='singlecomment'),
    path('singlecommentDelete/<int:comment_id>', views.singleCommentDelete, name='singlecommentDelete'),

    path('getintouch/', views.getintouch, name='getintouch'),
    path('deletegetintouch/<int:getintouch_id>', views.deletegetintouch, name='deletegetintouch'),
    path('singlegetintouch/<int:getintouch_id>', views.singlegetintouch, name='singlegetintouch'),

    path('newsLetter/', views.newsLetter, name='newsLetter'),
    path('nsingleewsLetter/<int:newslettermessage_id>', views.singlenewsLetter, name='singlenewsLetter'),
    path('sendemails/', views.sendEmails, name='sendemails'),

    path('account/', views.account, name='account'),
    path('updateaccount/', views.updateaccount, name='updateaccount'),
    path('updateaccountprofilepic/', views.updateaccountprofilepic, name='updateaccountprofilepic'),



  # useraccount password change
   path('user_account/change_password', views.change_password, name='change_password'),



    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset.html',
        email_template_name='password/password_reset_email.html',
        subject_template_name='password/password_reset_subject.txt',
        success_url=reverse_lazy('CCSBADMIN:password_reset_done')
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html',
    ), name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password/password_reset_confirm.html',
        success_url=reverse_lazy('CCSBADMIN:password_reset_complete')
    ), name='password_reset_confirm'),

    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html',
    ), name='password_reset_complete'),

]