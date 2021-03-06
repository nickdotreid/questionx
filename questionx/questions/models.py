from django.db import models

from django.db.models.signals import pre_save, post_save, pre_delete

from django.contrib.auth.models import User
from smsmessages.models import Phone

# Register your models here.
class Patient(Phone):
	user = models.OneToOneField(User, blank=True)

	def __unicode__(self):
		return "%s" % (self.phone_number)

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

def patient_welcome_message(sender, instance, created, **kwargs):
	if not created:
		return
	instance.send_sms('Welcome to Qx.')
post_save.connect(patient_welcome_message, sender=Patient)

def patient_delete_user(sender, instance, **kwargs):
	instance.user.delete()
pre_delete.connect(patient_delete_user, sender=Patient)

def patient_on_new_phone(sender, instance, created, **kwargs):
	if not created:
		return
	pat = Patient()
	pat.phone_number = instance.phone_number
	pat.save()
	instance.delete() # get rid of new instance, because Patient creates a new one (and this doesn't create a loop?)
post_save.connect(patient_on_new_phone, sender=Phone)


class Question(models.Model):

	text = models.CharField(max_length=250)
	created = models.DateField(auto_now_add=True)

	owner = models.ForeignKey(Patient)

	def __unicode__(self):
		return "(%s) %s" % (owner, self.text)
