from models import Econtaint, Media_containt
from django import forms

class FileForm(forms.ModelForm):
	class Meta:
	    model = Media_containt
	    fields = ['file']

class ContaintForm(forms.ModelForm):
	class Meta:
	    model = Econtaint
	    fields = ['name', 'tag', 'search_tags', 'content']

	def __init__(self, *args, **kwargs):
		super(ContaintForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'placeholder' : 'Containt Name', 'class' :'form-control'})
		self.fields['search_tags'].widget.attrs.update({'placeholder' : 'Search tag (comma seperated)', 'class' :'form-control'})
		self.fields['tag'].widget.attrs.update({'class' :'form-control'})
		self.fields['content'].widget.attrs.update({'class' :'form-control'})
	