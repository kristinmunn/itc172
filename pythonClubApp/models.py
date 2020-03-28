from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda
class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    location=models.TextField()
    agenda=models.TextField()

    def __str__(self):
        return self.meetingTitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

#Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text
class MeetingMinutes(models.Model):
    minutesTitle=models.CharField(max_length=255)
    meetingID=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutesText=models.TextField()

    def __str__(self):
        return self.minutesText
    
    class Meta:
        db_table='meeting_minutes'
        verbose_name_plural='meeting_minutes'
        
#Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description
class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    URL=models.URLField()
    dataEntered=models.DateField()
    userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourceName
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

#Event which will have fields for event title, location, date, time, description and the user id of the member that posted it
class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    location=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userID=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventTitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'
