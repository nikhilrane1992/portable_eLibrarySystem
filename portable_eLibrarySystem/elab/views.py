from django.shortcuts import render
from models import Econtaint
from forms import ContaintForm

# Create your views here.
def add_containt(request):
	if request.POST:
		containt_form = ContaintForm(request.POST)
		if containt_form.is_valid():
			containt_form.save()
			return HttpResponseRedirect('/carrier/add/')
		else:
			print containt_form.errors
	else:
		args = {}
		containt_form = ContaintForm()
		args['containt_form'] = containt_form
	return render_to_response('admin/add_carrier.html', args)
