import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Poll

def createPoll(question, days):
	"""
	Creates a poll given a question and number
	of days offset in which to publish
	"""
	return Poll.objects.create(question=question, pub_date=timezone.now() + datetime.timedelta(days=days))

class PollIndexDetailsTests(TestCase):
	def testDetailViewWithAFuturePoll(self):
		"""
		Future polls should throw a 404
		"""
		futurePoll = createPoll('Future Poll', days=30)
		response = self.client.get(reverse('polls:detail', args=(futurePoll.id,)))
		self.assertEqual(response.status_code, 404)

	def testDetailViewWithAPastPoll(self):
		"""
		Past polls should display the question
		"""
		pastPoll = createPoll('Past Poll', days=-30)
		response = self.client.get(reverse('polls:detail', args=(pastPoll.id,)))
		self.assertContains(response, 'Past Poll', status_code=200)

class PollViewTests(TestCase):
	def testIndexViewWithNoPolls(self):
		"""
		If no polls exist, correct message should be displayed
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No polls are available')
		self.assertQuerysetEqual(response.context['latestPollList'], [])

	def testIndexViewWithAPastPoll(self):
		"""
		Polls with a pub_date in the past should display on index page
		"""
		createPoll('Past Poll', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latestPollList'], ['<Poll: Past Poll>'])

	def testIndexViewWithAFuturePoll(self):
		"""
		Polls with a pub_date in the future should not be displayeds
		"""
		createPoll('Future Poll', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, 'No polls are available', status_code=200)
		self.assertQuerysetEqual(response.context['latestPollList'], [])

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