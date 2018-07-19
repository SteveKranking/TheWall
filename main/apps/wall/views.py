from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    return render(request, "wall/index.html")


def dashboard(request, first_name):
    context = {
      "messages": Message.objects.order_by("created_at"),
      "authors": Comment.objects.order_by("created_at"),
      'user': User.manager.get(id=req.session['id'])

    }
    
    return render(request, "wall/dashboard.html", context)


def login(req):
    
    context = {
      errors: 'errors'
    }

    result = User.manager.login(req.POST)
       
    return redirect('/')

def register(request):

    contect = {
      errors: 'errors'
    }

    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']

    new_user = self.create(email = 'email', password = 'password', username ='username')
   
    return redirect('/')

def message(req):
    
       
    return redirect('/')

def comment(req):
    
    return redirect('/')

