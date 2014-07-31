import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):

	def testWasPublishedRecentlyWithFuturePoll(self):
		"""
		was_published_recently() should return False for polls whose
		pub_date is in the future
		"""
		futurePoll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(futurePoll.was_published_recently(), False)