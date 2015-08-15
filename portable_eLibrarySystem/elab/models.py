from django.db import models

# Create your models here.

def get_upload_containt(instance, filename):
    return "Containt/%s" %(filename)

class Media_containt(models.Model):
	file = models.FileField(upload_to=get_upload_containt)
	def __unicode__(self):
		return str(self.file)

class Econtaint(models.Model):
	BOOK = 0
	VIDEO = 1
	CONTAINENTCHOICES = ((BOOK,'Book'),(VIDEO,'Video'))
	name = models.CharField(max_length=500)
	tag = models.IntegerField(choices=CONTAINENTCHOICES)
	search_tags = models.TextField()
	content = models.ForeignKey('Media_containt')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name + ' '+'Tag-->'+str(self.tag)