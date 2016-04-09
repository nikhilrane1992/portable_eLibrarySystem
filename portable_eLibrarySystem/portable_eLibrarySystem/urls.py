"""portable_eLibrarySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^elab/', include('elab.urls')),
    url(r'^admin_login/$','portable_eLibrarySystem.views.admin_login'),
    url(r'^admin_logout/$','portable_eLibrarySystem.views.admin_logout_view'),
    url(r'^user_logout/$','portable_eLibrarySystem.views.user_logout_view'),
    url(r'^auth/$','portable_eLibrarySystem.views.auth'),
    url(r'^login/status/$','portable_eLibrarySystem.views.check_login'),
    url(r'^landing/page/$','portable_eLibrarySystem.views.landing_page'),
    url(r'^partial_book/template/$','portable_eLibrarySystem.views.book_partial_page'),
    url(r'^render_quiz_tab/$','portable_eLibrarySystem.views.render_quiz_tab'),
    url(r'^$','portable_eLibrarySystem.views.render_login_page'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
