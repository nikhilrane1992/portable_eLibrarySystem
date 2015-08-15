from django.shortcuts import render
from models import Econtaint, Media_containt
from forms import ContaintForm, FileForm
from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
import json

# Create your views here.
def add_containt(request):
	args = {}
	if request.POST:
		try:
			request.POST['file_field']
			file_form = FileForm(request.POST, request.FILES)
			if file_form.is_valid():
				media_containt = Media_containt(file=request.FILES['file'])
				media_containt.save()
				print 'save and redirect'
				return HttpResponseRedirect('/elab/add/containt/')
			else:
				containt_form = ContaintForm()
				args['containt_form'] = containt_form
				args['file_form'] = file_form
				print file_form.errors
				return render_to_response('admin_template/admin_pannel.html', args)

		except Exception, e:
			print "Exception-->", e
			containt_form = ContaintForm(request.POST)
			if containt_form.is_valid():
				containt_form.save()
				return HttpResponseRedirect('/elab/add/containt/')
			else:
				file_form = FileForm()
				args['containt_form'] = containt_form
				args['file_form'] = file_form
				print containt_form.errors
				return render_to_response('admin_template/admin_pannel.html', args)
		
	else:
		containt_form = ContaintForm()
		file_form = FileForm()
		args['containt_form'] = containt_form
		args['file_form'] = file_form
	return render_to_response('admin_template/admin_pannel.html', args)

def send_tags(request):
	if request.user.is_authenticated():
		tag_list = []
		[tag_list.append({'tag':dict(Econtaint.CONTAINENTCHOICES)[i], 'id': i}) for i in dict(Econtaint.CONTAINENTCHOICES)]
		return HttpResponse(json.dumps({"tag_list": tag_list, "status": True}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"validation": "Your login credential invalid..!!", "status": False}), content_type="application/json")

def send_containt(request):
	if request.user.is_authenticated():
		data_dictonary = json.loads(request.body)
		tag_id = data_dictonary['tag_id']
		containt_objs = Econtaint.objects.filter(tag=tag_id)
		containt_list = []
		for i in containt_objs:
			containt_list.append({'name': i.name, 'media_url': '/Media/'+str(i.content)})
		return HttpResponse(json.dumps({"containt_list": containt_list, "status": True}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"validation": "Your login credential invalid..!!", "status": False}), content_type="application/json")
