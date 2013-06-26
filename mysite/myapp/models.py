# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.localflavor.us.models import USStateField

# Create your models here.

class Person(models.Model):
	SHIRT_SIZES = (
		(u'S' , u'Small'),
		(u'M' , u'Medium'),
		(u'L' , u'Large')
	)
	first_name = models.CharField("person's first name", max_length=30)
	last_name = models.CharField("person's last name", max_length=30)
	birth_date = models.DateField()
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = USStateField() # Yes, this is America-centric...
	shirt_size = models.CharField(max_length=2,choices=SHIRT_SIZES)

	def __unicode__(self):
		return self.first_name

	def baby_boomer_status(self):
		"Return the person's baby-boomer status."
		import datetime
		if datetime.date(1945,8,1) <= self.birth_date <= datetime.date(1964,12,31):
			return "Baby boomer"
		if self.birth_date < datetime.date(1945,8,1):
			return "Post-boomer"
		return "Post-boomer"

	def is_midwestern(self):
		"Return True if this person is from the Midwest."
		return self.state in ('IL','WI','MI','IN','OH','IA','MO')

	def _get_full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.first_name, self.last_name)
	full_name = property(_get_full_name)



class Musician(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	instrument = models.CharField(max_length=100)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Album(models.Model):
	artist = models.ForeignKey(Musician)
	name = models.CharField(max_length=100)
	release_date = models.DateField()
	nsum_stars = models.IntegerField()


class Manufacturer(models.Model):
	name = models.CharField('制造厂',max_length=50)	
	www = models.CharField('网址',max_length=100)

	def __unicode__(self):
		return self.name

class Car(models.Model):
	manufacturer = models.ForeignKey(Manufacturer,verbose_name='制造厂')
	name = models.CharField('汽车品牌',max_length=30)

	def __unicode__(self):
		return self.name

class Student(models.Model):
	name = models.CharField('姓名',max_length=20)	
	def __unicode__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField('姓名',max_length=20)
	students = models.ManyToManyField(Student)

	def __unicode__(self):
		return self.name


class Publication(models.Model):
	title = models.CharField(max_length=30)

	def __unicode__(self):
			return self.title

	class Meta:
		ordering = ('title',)

class Article(models.Model):
	headline = models.CharField(max_length=100)
	publications = models.ManyToManyField(Publication)

	def __unicode__(self):
		return self.headline

	class Meta:
		ordering = ('headline',)
	

'''
One-to-one relationships
'''

class Place(models.Model):
	name = models.CharField(max_length=50)
	addr = models.CharField(max_length=80)

	def __unicode__(self):
		return u"%s the place" % self.name

class Restaurant(models.Model):
	place = models.OneToOneField(Place, primary_key=True)
	serves_hot_dogs = models.BooleanField()
	serves_pizza = models.BooleanField()

	def __unicode__(self):
		return u"%s the restaurant" % self.place.name

class Waiter(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return u"%s waiter at %s" % (self.name, self.restaurant)



	
