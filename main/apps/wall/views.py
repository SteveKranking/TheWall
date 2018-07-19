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
    
    errors = []

    email = request.POST['email']
    password = reqiest.POST['password']

    called_user = User.objects.get(email="email")

    if(called_user == null):
      errors.append("Username not found")
    elif(called_user.password != password):
      errors.append("Password incorrect")
      return redirect('/')
    
    else:
      
      request.session['user'] = User.objects.get(email="email")

      return redirect('/dashboard')

def register(request):

    context = {
      errors: 'errors'
    }

    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']

    new_user = self.create(email = 'email', password = 'password', username ='username')
   
    return redirect('/')

def message(req):

    context = {
      errors: 'errors'
    }    
    content = request.POST['content']
    poster = request.session['user']

    new_message = self.create(content = 'content', poster = 'poster')
       
    return redirect('/')

def comment(req):

    context = {
      errors: 'errors'
    }

    content = request.POST['content']
    poster = request.session['user']

    new_comment = self.create(content = 'content', poster = 'poster')

    return redirect('/')

