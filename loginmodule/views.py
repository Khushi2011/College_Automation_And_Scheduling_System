from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render,render_to_response
# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticat(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/logintestapp/loggedin/')
    else:
        return HttpResponseRedirect('/logintestapp/invalidlogin/')

def loggedin(request):
    return render(request,'loggedin.html',{"full name":request.user.username})

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
