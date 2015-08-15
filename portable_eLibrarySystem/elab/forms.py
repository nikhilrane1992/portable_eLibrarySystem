from models import Econtaint
from django import forms

class ContaintForm(forms.ModelForm):
	class Meta:
	    model = Econtaint
	    fields = ['name', 'tag', 'search_tag', 'content']

	def __init__(self, *args, **kwargs):
		super(Econtaint, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'placeholder' : 'Containt Name', 'class' :'form-control'})
		self.fields['search_tag'].widget.attrs.update({'placeholder' : 'Search tag (comma seperated)', 'class' :'form-control'})
		
		## set empty label for dropdown
		self.fields['tag'].empty_label = "please choose tag"