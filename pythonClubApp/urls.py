from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getmeeting/', views.getmeeting, name='meeting'),
    path('meeting_details/<int:id>', views.meetingDetails, name='meeting_details'),
    path('resource/', views.resource, name='resource'),
    path('event/', views.event, name='event'),
    path('loginmessage/', views.loginMessage, name='loginmessage'), 
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('newMeetingMinutes/', views.newMeetingMinutes, name='newmeetingminutes')

]



