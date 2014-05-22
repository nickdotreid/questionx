from django.db import models

from questions.models import Patient

class Appointment(models.Model):

	owner = models.ForeignKey(Patient)
	confirmed = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	date = models.DateTimeField()

	title = models.CharField(null=True, max_length=150)
