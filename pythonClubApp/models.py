from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.TextField()
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

#Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text
class MeetingMinutes(models.Model):
    minutestitle=models.CharField(max_length=255)
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.minutestitle
    
    class Meta:
        db_table='meetingminutes'

#Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description
class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceURL=models.URLField()
    resourcedataentered=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'

#Event which will have fields for event title, location, date, time, description and the user id of the member that posted it
class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField()
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
