from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
from localflavor.us.forms import USPhoneNumberField
import phonenumbers

from smsmessages.models import Phone

from smsmessages.signals import smsmessage

def recieve(request):
	if 'From' in request.REQUEST and 'Body' in request.REQUEST:
		phone = False
		for ph in Phone.objects.filter(phone_number=request.REQUEST['From'])
			phone = ph
		if not phone:
			phone = Phone(phone_number=request.REQUEST['From'])
			phone.save()
		smsmessage.send(
			sender=False,
			phone=Phone,
			message=request.REQUEST['Body']
			)
	return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><Response></Response>')

def send(request, phone_number):
	phone = get_object_or_404(Phone, phone_number=phone_number)

def list(request, phone_number):
	phone = get_object_or_404(Phone, phone_number=phone_number)