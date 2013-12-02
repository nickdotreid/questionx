from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
import phonenumbers

from questions.models import Patient

class JoinForm(forms.Form):
	phone_number = forms.CharField(max_length=25, required=True)

def join(request):
	form = JoinForm()
	if request.POST:
		form = JoinForm(request.POST)
		if form.is_valid():
			patient = Patient()
			patient.phone_number = form.cleaned_data['phone_number']
			try:
				patient.save()
				# start patient session
				return HttpResponseRedirect(reverse(view, kwargs={'phone_number':patient.phone_number}))
			except:
				pass
	return render_to_response('pages/join.html',{
		'form':form,
		},context_instance=RequestContext(request))

def view(request, phone_number):
	patient = get_object_or_404(Patient, phone_number=phone_number)

	return render_to_response('pages/join.html',{
		},context_instance=RequestContext(request))