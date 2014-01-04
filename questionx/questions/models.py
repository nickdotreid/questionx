from django.db import models

from django.db.models.signals import pre_save

from django.contrib.auth.models import User
from smsmessages.models import Phone

# Register your models here.
class Patient(Phone):
	user = models.OneToOneField(User, blank=True)

	def __unicode__(self):
		return "Patient: %s" % (self.phone_number)

def patient_create_user_if_null(sender, instance, **kwargs):
	if 'raw' in kwargs and kwargs['raw']:
		return
	try:
		instance.user
	except:
		user = User(username=instance.phone_number)
		user.save()
		instance.user = user
pre_save.connect(patient_create_user_if_null, sender=Patient)


class Question(models.Model):

	text = models.CharField(max_length=250)
	created = models.DateField(auto_now_add=True)

	owner = models.ForeignKey(Patient)

	def __unicode__(self):
		return "(%s) %s" % (owner, self.text)
