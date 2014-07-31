import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):

	def testWasPublishedRecentlyWithFuturePoll(self):
		"""
		wasPublishedRecently() should return False for polls whose
		pub_date is in the future
		"""
		futurePoll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(futurePoll.wasPublishedRecently(), False)

	def testWasPublishedRecentlyWithOldPoll(self):
		"""
		wasPublishedRecently() should return False for polls created more
		than a month ago
		"""
		pastPoll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(pastPoll.wasPublishedRecently(), False)

	def testWasPublishedRecentlyWithNewPoll(self):
		"""
		wasPublishedRecently() should return False for polls created
		within the last hour
		"""
		newPoll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(newPoll.wasPublishedRecently(), True)