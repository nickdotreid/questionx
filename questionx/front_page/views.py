from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from appointments.views import AppointmentForm

# Create your views here.
def signup(request):
	return render_to_response('front_page/signup.html',{
		'form': AppointmentForm(),
		}, context_instance=RequestContext(request))