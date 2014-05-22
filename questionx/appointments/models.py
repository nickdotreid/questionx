from django.db import models

from questions.models import Patient

class Appointment(models.Model):

	owner = models.ForeignKey(Patient)
	confirmed = models.BooleanField(default=False)

	date = models.DateTimeField()

	title = models.CharField(null=True, blank=True, max_length=150)
