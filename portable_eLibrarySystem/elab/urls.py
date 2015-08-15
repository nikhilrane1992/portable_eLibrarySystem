from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [   
    url(r'^add/containt/$','elab.views.add_containt'),
    url(r'^get/all/tags/$','elab.views.send_tags'),
    url(r'^get/containt/$','elab.views.send_containt'),
]
