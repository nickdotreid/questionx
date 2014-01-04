from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django import forms
from localflavor.us.forms import USPhoneNumberField
import phonenumbers

from questions.models import Patient, Question

class JoinForm(forms.Form):
	phone_number = USPhoneNumberField(required=True)

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['text']

def join(request):
	form = JoinForm()
	if request.POST:
		form = JoinForm(request.POST)
		if form.is_valid():
			phone_representation = phonenumbers.parse(form.cleaned_data['phone_number'], "US")

			patient = Patient()
			patient.phone_number = phonenumbers.format_number(phone_representation, phonenumbers.PhoneNumberFormat.E164)
			try:
				patient.save()
				# start patient session
				patient.send_sms('Welcome to Qx.')
				return HttpResponseRedirect(reverse(view, kwargs={'phone_number':patient.phone_number}))
			except:
				pass
	return render_to_response('pages/join.html',{
		'form':form,
		},context_instance=RequestContext(request))

def view(request, phone_number):
	patient = get_object_or_404(Patient, phone_number=phone_number)
	questions = Question.objects.filter(owner=patient).all().reverse()
	return render_to_response('pages/list.html',{
		'patient':patient,
		'questions':questions,
		},context_instance=RequestContext(request))

def create(request, phone_number):
	patient = get_object_or_404(Patient, phone_number=phone_number)
	form = QuestionForm()
	if request.POST:
		form = QuestionForm(request.POST)
		if form.is_valid():
			question = form.save(commit=False)
			question.owner = patient
			question.save()
			return HttpResponseRedirect(reverse(view, kwargs={'phone_number':patient.phone_number}))
	return render_to_response('questions/form.html',{
		'form':form,
		}, context_instance=RequestContext(request))

def edit(request, phone_number, question_id):
	question = get_object_or_404(Question, id=question_id)
	patient = get_object_or_404(Patient, phone_number=phone_number)
	form = QuestionForm(instance=question)
	if request.POST:
		form = QuestionForm(request.POST, instance=question)
		if form.is_valid():
			question = form.save()
			return HttpResponseRedirect(reverse(view, kwargs={'phone_number':patient.phone_number}))
	return render_to_response('questions/form.html',{
		'form':form,
		'question': question,
		}, context_instance=RequestContext(request))

def delete(request, phone_number, question_id):
	question = get_object_or_404(Question, id=question_id)
	patient = get_object_or_404(Patient, phone_number=phone_number)

	question.delete()

	return HttpResponseRedirect(reverse(view, kwargs={'phone_number':patient.phone_number}))