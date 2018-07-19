from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
  return render(request, "wall/index.html")


def dashboard(request, first_name):
  
  context = {
    'user': request.session['user']
  }

  # if(len(Message.objects.all()) > 0):
  #   context.["messages": Message.objects.order_by("created_at")]
  # if(len(Comment.objects.all()) > 0):
  #   context.["comments": Comment.objects.order_by("created_at")]

  
  return render(request, "wall/dashboard.html", context)


def login(request):
    
  # context = {
  #   errors: 'errors'
  # }
  
  errors = []

  email = request.POST['email']
  password = request.POST['password']

  try:
    user = User.objects.get(email=email)
  except User.DoesNotExist:
    user = None
    errors.append("Username not found")
  if(type(user) == None):
    if(user.password != password):
      errors.append("Password Incorrect")
    return redirect('/')
  
  else:    
    request.session['user'] = User.objects.get(email = email)
    return redirect('/dashboard')

def register(request):

  # errors = []

  # context = {
  #   errors: 'errors'
  # }

  email = request.POST['email']
  password = request.POST['password']
  username = request.POST['username']

  new_user = User.objects.create(email = email, password = password, username = username)

  print(new_user.username)
  
  
  return redirect('/')

def message(req):


  # errors = []

  # context = {
  #   errors: 'errors'
  # }  

  content = request.POST['content']
  poster = request.session['user']

  new_message = Message.objects.create(content = 'content', poster = 'poster')
      
  return redirect('/')

def comment(req):

  # errors = []
  
  # context = {
  #   errors: 'errors'
  # }

  content = request.POST['content']
  poster = request.session['user']

  new_comment = Comment.objects.create(content = 'content', poster = 'poster')

  return redirect('/')

def logout(request):
  request.session.flush()
  return redirect('/')