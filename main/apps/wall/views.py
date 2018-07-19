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
    
 check = User.objects.login(
      request.POST["username"],
      request.POST["password"]
  )

  if not check["valid"]:
      for error in check["errors"]:
          messages.add_message(request, messages.ERROR, error)
      return redirect("/")
  else:
      request.session["user_id"] = check["username"].id
      messages.add_message(request, messages.SUCCESS, "Welcome, {}".format(check["username"].name))
      return redirect("/dashboard")

def register(request):

  check = User.objects.register(
         request.POST["username"],
        request.POST["email"],
        request.POST["password"]
    )

  if not check["valid"]:
      for error in check["errors"]:
          messages.add_message(request, messages.ERROR, error)
      return redirect("/")
  else:
      request.session["user_id"] = check["user"].id
      messages.add_message(request, messages.SUCCESS, "Welcome, {}".format(request.POST["username"]))
      return redirect("/")
  
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