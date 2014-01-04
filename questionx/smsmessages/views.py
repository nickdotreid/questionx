from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
from localflavor.us.forms import USPhoneNumberField
import phonenumbers

from smsmessages.models import Phone

def recieve(request):
	if request.POST:
		pass

def send(request, phone_number):
	phone = get_object_or_404(Phone, phone_number=phone_number)

def list(request, phone_number):
	phone = get_object_or_404(Phone, phone_number=phone_number)