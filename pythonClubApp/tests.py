from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event, User
from django.urls import reverse
from .views import index, meeting, meetingdetails, resource, event
from .forms import MeetingForm, ResourceForm, MeetingMinutesForm


class MeetingTest(TestCase):
    def test_string(self):
        meetingTitle=Meeting(meetingTitle='Annual Meeting')
        self.assertEqual(str(meetingTitle), meetingTitle.meetingTitle)
 
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')
    
    def setUp(self):
       meeting=Meeting(agenda='Voting on new mascot', location='Seattle Central College', meetingDate='2020-04-26', meetingTime='02:00 pm')
       return meeting
    
    def test_type(self):
        meeting=self.setUp()
        self.assertEqual(str(meeting.agenda), 'Voting on new mascot')

    def test_string_location(self):
        meeting=self.setUp()
        self.assertEqual(str(meeting.location), 'Seattle Central College')
    
    def test_string_date_time(self):
        meeting=self.setUp()
        self.assertEqual(str(meeting.meetingTime), '02:00 pm')
        self.assertEqual(str(meeting.meetingDate), '2020-04-26')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutesText=MeetingMinutes(minutesText='Agreed on the Bald Eagle')
        self.assertEqual(str(minutesText), minutesText.minutesText)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meeting_minutes')

class ResourceTest(TestCase):
    def test_string(self):
        resourceName=Resource(resourceName='Votes')
        self.assertEqual(str(resourceName), resourceName.resourceName)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

    def setUp(self):
        self.user=User.objects.create(username='Steve')
        self.resource=Resource(resourceName='Django Models', resourceType='offical Django documentation', url='https://docs.djangoproject.com/en/3.0/topics/db/models/', dateEntered='2020-01-23', userID=self.user, description='This is offical documentation on creating Django Models')
    
    def test_string_user(self):
        self.assertEqual(str(self.user), self.resource.userID.get_username())

    def test_string_url(self):
        url=self.resource.url
        self.assertEqual(str(url), 'https://docs.djangoproject.com/en/3.0/topics/db/models/')

class EventTest(TestCase):
    def test_string(self):
        eventTitle=Event(eventTitle='PyDay')
        self.assertEqual(str(eventTitle), eventTitle.eventTitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class ResourceViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('resource'))
        self.assertEqual(response.status_code, 200)

class MeetingViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('meeting'))
        self.assertEqual(response.status_code, 200)

class EventViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('event'))
        self.assertEqual(response.status_code, 200)

class MeetingDetailsViewTest(TestCase):
    def setUp(self):
        self.meeting=Meeting.objects.create(meetingTitle='Annual PyDay', meetingDate='2020-03-14', meetingTime='12:00 PM', location='Pagliacci Pizza', agenda='Pepperoni!')

    def test_meeting_details_success(self):
        response=self.client.get(reverse('meeting_details', args=(self.meeting.id,)))
        self.assertEqual(response.status_code, 200)

class MeetingFormTest(TestCase):
    def test_typeform_is_valid(self):
        form=MeetingForm(data={'meetingTitle': "test", 'meetingDate': "2020-02-18", 'meetingTime': "13:00", 'location': "community center", 'agenda': "django"})
        self.assertTrue(form.is_valid())
    
    def test_typeform_empty(self):
        form=MeetingForm(data={'meetingTitle': "", 'meetingDate': "", 'meetingTime': "", 'location': "", 'agenda': ""})
        self.assertFalse(form.is_valid())

class ResourceFormTest(TestCase):
    def test_typeform_is_valid(self):
        user=User.objects.create(pk=1).pk
        
        form=ResourceForm(data={'resourceName': "Django", 'resourceType': "Testing in Django", 'url': "https://docs.djangoproject.com/en/3.0/topics/testing/", 'dateEntered': "2020-06-23", 'userID': user, 'description': "Testing in Django"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=ResourceForm(data={'resourceName': "", 'resourceType': "", 'url': "", 'dateEntered': "", 'userID': "", 'description': ""})
        self.assertFalse(form.is_valid())

class MeetingMinutesFormTest(TestCase):
    def setUp(self):
        User.objects.create(username='Steve')
        User.objects.create(username='Kristin')
        User.objects.create(username='Toni')
        self.meeting=Meeting.objects.create(meetingTitle='Annual PyDay', meetingDate='2020-03-14', meetingTime='12:00 PM', location='Pagliacci Pizza', agenda='Pepperoni!')

    def test_typeform_is_valid(self):
        self.users = User.objects.all()
        form=MeetingMinutesForm(data={'meetingID': self.meeting.id, 'attendance': self.users, 'minutesText': 'This is a test.'})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=MeetingMinutesForm(data={'meetingID': "" , 'attendance': "", 'minutesText': ""})
        self.assertFalse(form.is_valid())

class NewMeetingAuthTest(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meeting=Meeting.objects.create(meetingTitle='Annual PyDay', meetingDate='2020-03-14', meetingTime='12:00 PM', location='Pagliacci Pizza', agenda='Pepperoni!')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonApp/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pythonApp/newmeeting.html')

class NewResourceAuthTest(TestCase):
    def setUp(self):
        self.test_user= User.objects.create_user(username='testuser2', password='P@ssw0rd2')
        self.resource= Resource.objects.create(resourceName='Django Models', resourceType='offical Django documentation', url='https://docs.djangoproject.com/en/3.0/topics/db/models/', dateEntered='2020-01-23', userID=self.test_user, description='This is offical documentation on creating Django Models')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonApp/newResource/')
    
    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser2', password='P@ssw0rd2')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pythonApp/newresource.html')
