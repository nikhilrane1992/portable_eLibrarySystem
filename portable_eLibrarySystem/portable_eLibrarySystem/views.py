from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
import json
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

## book partial page
def book_partial_page(request):
    return render_to_response('html_template/partials/books.html')

## rendering admin login page
def admin_login(request):
    return render_to_response('html_template/admin_template/adminPanelLogin.html')

## login in our system
def auth(request):
    data_dictonary = json.loads(request.body)
    username = data_dictonary['username']
    password = data_dictonary['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # user_status = is_member(user)
            # print "user_status-->", user_status
            return HttpResponse(json.dumps({"username":username,"url": '/landing/page/', "status": True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"validation": "Invalid login details", "status": False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation": "Invalid login details", "status": False}), content_type="application/json")

## logout url
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

## check user login or not status
def check_login(request):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        return HttpResponse(json.dumps({"username": user.username, "status": True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status": False}), content_type="application/json")

## home page
def landing_page(request):
    if request.user.is_authenticated():
        return render_to_response('html_template/user_template/index.html')

## render Quiz Tab
def render_quiz_tab(request):
    return render_to_response('html_template/partials/quiz.html')
