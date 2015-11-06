from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [   
    url(r'^add/containt/$','elab.views.add_containt'),
    url(r'^get/all/tags/$','elab.views.send_tags'),
    url(r'^get/containt/$','elab.views.send_containt'),
    url(r'^quiz_admin_page/$','elab.views.quiz_admin_page'),
    url(r'^save_question/$','elab.views.save_question_options'),
    url(r'^get_question_and_answer/$','elab.views.get_question_and_answer'),
]
