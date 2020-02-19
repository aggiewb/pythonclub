from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event, User
from django.urls import reverse
from .views import index, meeting, meetingDetails, resource, event
from .form import MeetingForm, ResourceForm


class MeetingTest(TestCase):
    def test_string(self):
        meetingTitle=Meeting(meetingTitle='Annual Meeting')
        self.assertEqual(str(meetingTitle), meetingTitle.meetingTitle)
 
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')
    
    def setUp(self):
       meeting=Meeting(agenda='Voting on new club board members', location='Community Center', meetingDate='2020-06-23', meetingTime='03:00 pm')
       return meeting
    
    def test_type(self):
        meeting = self.setUp()
        self.assertEqual(str(meeting.agenda), 'Voting on new club board members')

    def test_string_location(self):
        meeting=self.setUp()
        self.assertEqual(str(meeting.location), 'Community Center')
    
    def test_string_date_time(self):
        meeting=self.setUp()
        self.assertEqual(str(meeting.meetingTime), '03:00 pm')
        self.assertEqual(str(meeting.meetingDate), '2020-06-23')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutesText=MeetingMinutes(minutesText='Susie Sue was voted in as board president')
        self.assertEqual(str(minutesText), minutesText.minutesText)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meeting_minutes')

class ResourceTest(TestCase):
    def test_string(self):
        resourceName=Resource(resourceName='Offical Documentation')
        self.assertEqual(str(resourceName), resourceName.resourceName)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

    def setUp(self):
        self.user=User.objects.create(username='Steve')
        self.resource=Resource(resourceName='Django Models', resourceType='offical Django documentation', url='https://docs.djangoproject.com/en/3.0/topics/db/models/', dateEntered='2020-01-23', userID=self.user, description='This is offical documentation on creating Django Models')
    
    def test_string_user(self):
        self.assertEqual(str(self.user), self.resource.userID.get_username())

    def test_string_url(self):
        url = self.resource.url
        self.assertEqual(str(url), 'https://docs.djangoproject.com/en/3.0/topics/db/models/')

class EventTest(TestCase):
    def test_string(self):
        eventTitle=Event(eventTitle='PyDay')
        self.assertEqual(str(eventTitle), eventTitle.eventTitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class ResourceViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resource'))
        self.assertEqual(response.status_code, 200)

class MeetingViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meeting'))
        self.assertEqual(response.status_code, 200)

class EventViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('event'))
        self.assertEqual(response.status_code, 200)

class MeetingDetailsViewTest(TestCase):
    def setUp(self):
        self.meeting=Meeting.objects.create(meetingTitle='Annual PyDay', meetingDate='2020-03-14', meetingTime='10:00 AM', location='Elysian Brewery', agenda='The theme for 2020 is Django!') 

    def test_meeting_details_success(self):
        response = self.client.get(reverse('meeting_details', args=(self.meeting.id,)))
        self.assertEqual(response.status_code, 200)







