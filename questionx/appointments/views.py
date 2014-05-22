from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
from localflavor.us.forms import USPhoneNumberField
import phonenumbers

class AppointmentForm(forms.Form):
	phone_number = USPhoneNumberField(required=True)
	date = forms.DateTimeField()

# Create your views here.
def create(request):
	form = AppointmentForm()
	if request.POST:
		form = AppointmentForm(request.POST)
		if form.is_valid():
			phone_representation = phonenumbers.parse(form.cleaned_data['phone_number'], "US")
			# get phone owner (or create then)
			
			# make sure appointment date is in the future

			# create appointment
			# send confirm sms message

			# redirect to detail view
	return render_to_response('appointments/create.html',{
		'form':form,
		},context_instance=RequestContext(request))
