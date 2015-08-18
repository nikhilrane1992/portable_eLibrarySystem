from django.shortcuts import render
from models import Econtaint, Media_containt
from forms import ContaintForm, FileForm
from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
import json
import subprocess
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_files_url = BASE_DIR + "/Media/Containt/"


# Create your views here.
def add_containt(request):
	args = {}
	if request.POST:
		try:
			request.POST['file_field']
			file_form = FileForm(request.POST, request.FILES)
			if file_form.is_valid():
				file_name = request.FILES['file']
				media_containt = Media_containt(file=file_name)
				media_containt.save()
				pdf_file_name = str(file_name).replace(' ', '_')
				image_file_name = str(file_name).replace(' ', '_').split('.')
				image_file_name[-1] = 'png'
				image_file_name = '.'.join(image_file_name)
				cmd = 'gs -o '+media_files_url+image_file_name+' -sDEVICE=pngalpha -dLastPage=1 '+media_files_url+pdf_file_name
				print cmd
				subprocess.call(cmd, shell=True)
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
			media_pdf_url = i.content
			media_img_url = str(i.content).split('.')
			media_img_url[-1] = 'png'
			media_img_url = '.'.join(media_img_url)
			containt_list.append({'name': i.name, 'media_pdf_url': '/Media/'+str(media_pdf_url), 'media_img_url': '/Media/' + media_img_url})
		return HttpResponse(json.dumps({"containt_list": containt_list, "status": True}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"validation": "Your login credential invalid..!!", "status": False}), content_type="application/json")
