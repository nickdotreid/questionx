from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
from localflavor.us.forms import USPhoneNumberField
import phonenumbers

from smsmessages.models import Phone

from smsmessages.signals import smsmessage

from django import forms
from localflavor.us.forms import USPhoneNumberField
import phonenumbers

class RecieveForm(forms.Form):
	From = USPhoneNumberField(required=True)
	Body = forms.CharField(required=False)
	redirect_to = forms.CharField(
		required = False,
		widget = forms.HiddenInput(),
		)

def recieve(request):
	form = RecieveForm(initial={'redirect_to':reverse(recieve)})
	if 'From' in request.REQUEST and 'Body' in request.REQUEST:
		form = RecieveForm(request.REQUEST)
		if form.is_valid():
			phone_representation = phonenumbers.parse(form.cleaned_data['From'], "US")
			phone_number = phonenumbers.format_number(phone_representation, phonenumbers.PhoneNumberFormat.E164)
			phone, created = Phone.objects.get_or_create(phone_number=phone_number)
			smsmessage.send(
				sender=False,
				phone=phone,
				message=request.REQUEST['Body']
				)
			if 'redirect_to' in request.REQUEST:
				return HttpResponseRedirect(request.REQUEST['redirect_to'])
			return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><Response></Response>')
	return render_to_response('questions/form.html',{
		'form':form,
		}, context_instance=RequestContext(request))

def send(request, phone_number):
	phone = get_object_or_404(Phone, phone_number=phone_number)

def list(request, phone_number):
	phone = get_object_or_404(Phone, phone_number=phone_number)