from django.db import models
import datetime

# Create your models here.
from django.utils import timezone

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question

	def was_published_recently(self):
		# return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
		now = timezone.now()
		return now - datetime.timedelta(days = 1) <= self.pub_date < now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'published recently?'


		


class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()

	def __unicode__(self):
		return self.choice


