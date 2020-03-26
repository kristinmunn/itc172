from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm, MeetingMinutesForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'pythonApp/index.html')

def getmeeting(request):
    meeting=Meeting.objects.all()
    return render(request, 'pythonApp/meeting.html' ,{'meeting' : meeting})

def meetingDetails(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    detail={
        'meeting': meeting,
        'MeetingMinutes': MeetingMinutes,
    }
    return render(request, 'pythonApp/meeting_details.html', context = details)
#

def resource(request):
    resource = Resource.objects.all()
    return render(request, 'pythonApp/resource.html', {'resource' : resource})

def event(request):
    event = Event.objects.all()
    return render(request, 'pythonApp/event.html', {'event' : event})

def loginMessage(request):
    return render(request, 'pythonApp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'pythonApp/logoutmessage.html')

@login_required    
def newMeeting(request):
    meeting_form=MeetingForm
    if request.method=='POST':
        meeting_form=MeetingForm(request.POST)
        if meeting_form.is_valid():
            meetingPost=meeting_form.save(commit=True)
            meetingPost.save()
            meeting_form=MeetingForm()
    else:
        meeting_form=MeetingForm()
    return render(request, 'pythonApp/newmeeting.html', {'meeting_form': meeting_form})

@login_required
def newResource(request):
    resource=ResourceForm
    if request.method=='POST':
        resource=ResourceForm(request.POST)
        if resource.is_valid():
            resourcePost=resource.save(commit=True)
            resourcePost.save()
            resource=ResourceForm()
    else:
        resource=ResourceForm()
    return render(request, 'pythonApp/newresource.html', {'resource': resource})

@login_required
def newMeetingMinutes(request):
    minutes=MeetingMinutesForm
    if request.method=='POST':
        minutes=MeetingMinutesForm(request.POST)
        if minutes.is_valid():
            minutesPost=minutes.save(commit=True)
            minutesPost.save()
            minutes=MeetingMinutesForm()
    else:minutes=MeetingMinutesForm()
    return render(request, 'pythonApp/newmeetingminutes.html', {'minutes': minutes}) 
