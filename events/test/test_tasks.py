import arrow
from django.conf import settings
from django.core import mail
from django.utils import timezone

from events.models import Client, Event
from events.tasks import event_autoclose_task, event_notifications_task
from mailing.models import Sms
from vishleva.lib.test import TaskTestCase


class EventsTasksTest(TaskTestCase):
    def setUp(self):
        super(TaskTestCase, self).setUp()
        self.now = timezone.now()

        client = Client()
        client.email = 'client@example.com'
        client.phone = '79251111111'
        client.save()

        event = Event()
        event.begin = self.now + timezone.timedelta(hours=3)
        event.end = self.now + timezone.timedelta(hours=6)
        event.title = 'test_title_now'
        event.status = 'open'
        event.client = client
        event.save()

    def test_event_notifications_task(self):
        """
        Test event_notifications_task
        """

        event_notifications_task.delay()
        self.assertEqual(len(mail.outbox), 2)
        event = Event.objects.first()
        self.assertEqual(
            mail.outbox[0].subject,
            settings.EMAIL_SUBJECT_PREFIX + 'Upcoming event - ' + event.title)
        self.assertEqual(mail.outbox[1].subject, settings.EMAIL_SUBJECT_PREFIX
                         + 'Напоминание о предстоящей фотосессии')
        self.assertNotEqual(event.notified_at, None)
        begin = arrow.get(event.begin).to(settings.TIME_ZONE).datetime
        sms = Sms.objects.first()
        self.assertTrue(begin.strftime('%d.%m.%Y %H:%M') in sms.text)


class EventsFixturesTasksTest(TaskTestCase):
    fixtures = ['tests/events.json']

    def test_event_autoclose_task(self):
        """
        Test event_autoclose_task
        """
        event_autoclose_task.delay()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         settings.EMAIL_SUBJECT_PREFIX + 'Auto closed events')
        events = Event.objects.get_for_closing()
        self.assertEqual(events.count(), 0)
