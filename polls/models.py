from django.db import models
from django.utils import timezone
import datetime

class Poll(models.Model):
	def __unicode__(self):
		return self.question
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def wasPublishedRecently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now
	wasPublishedRecently.admin_order_field = 'pub_date'
	wasPublishedRecently.boolean = True
	wasPublishedRecently.short_description = 'Published Recently?'

class Choice(models.Model):
	def __unicode__(self):
		return self.choice_text
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
