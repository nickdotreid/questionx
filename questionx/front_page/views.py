from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

# Create your views here.
def signup(request):
	return render_to_response('front_page/signup.html',{}, context_instance=RequestContext(request))