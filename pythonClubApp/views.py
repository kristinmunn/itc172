from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import render

# Create your views here.
# Create your views here.
def index (request):
    return render(request, 'pythonApp/index.html')

def getmeeting(request):
    type_list=Meeting.objects.all()
    return render(request, 'pythonApp/meeting.html' ,{'type_list' : type_list})
