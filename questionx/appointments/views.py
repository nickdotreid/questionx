from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from localflavor.us.forms import USPhoneNumberField
import phonenumbers

from appointments.models import Appointment
from questions.models import Patient

from datetime import datetime
from django.utils.timezone import utc

class AppointmentForm(forms.Form):
	phone_number = USPhoneNumberField(required=True)
	date = forms.DateTimeField()

	def __init__(self, *args, **kwargs):
		super(AppointmentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_action = reverse(create)

		self.helper.add_input(Submit('submit', 'Submit'))

# Create your views here.
def create(request):
	form = AppointmentForm()
	if request.POST:
		form = AppointmentForm(request.POST)
		if form.is_valid():
			phone_representation = phonenumbers.parse(form.cleaned_data['phone_number'], "US")
			# get phone owner (or create then)
			patient = Patient.objects.get_or_create(phone_number=phone_representation)[0]
			
			# make sure appointment date is in the future
			now = datetime.utcnow().replace(tzinfo=utc)
			app_date = form.cleaned_data['date']
			if now < app_date:
				appointment = Appointment(
					owner=patient,
					date = app_date,
					)
				appointment.save()
				patient.send_sms('You added an appointment!')
				return HttpResponseRedirect(reverse(create))
	return render_to_response('appointments/create.html',{
		'form':form,
		},context_instance=RequestContext(request))
