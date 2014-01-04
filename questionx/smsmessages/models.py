from django.db import models

class Phone(models.Model):
	class Meta:
		abstract = True
	phone_number = models.CharField(blank=True, max_length=25)

	def __unicode__(self):
		return "Phone Number: %s" % (self.phone_number)