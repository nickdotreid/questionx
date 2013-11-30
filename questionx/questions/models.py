from django.db import models

from django.contrib.auth.models import User

class Patient(models.Model):

	user = models.OneToOneField(User, blank=True)
	phone_number = models.CharField(blank=True, max_length=25)

	def __unicode__(self):
		return self.phone_number


# Register your models here.
class Question(models.Model):

	text = models.CharField(max_length=250)
	created = models.DateField()

	owner = models.ForeignKey(Patient)

	def __unicode__(self):
		return "(%s) %s" % (owner, self.text)
