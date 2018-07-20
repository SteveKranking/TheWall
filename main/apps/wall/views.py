from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
  return render(request, "wall/index.html")


def dashboard(request, first_name):
  
  context = {
    'user': request.session['user'],
    "messages": Message.objects.order_by("created_at"),
    "comments": Comment.objects.order_by("created_at")
  }
  
  return render(request, "wall/dashboard.html", context)


def login(request):
    
  check = User.objects.login(
    request.POST["email"],
    request.POST["password"]
  )

  if not check["valid"]:
    for error in check["errors"]:
      messages.add_message(request, messages.ERROR, error)
    return redirect("/")
  else:
    request.session["user_id"] = check["email"].id
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
      # context = {
      #   errors: 'errors'
      # }
    return redirect("/")
  else:
    request.session["user_id"] = check["user"].id
    messages.add_message(request, messages.SUCCESS, "Welcome, {}".format(request.POST["username"]))
    return redirect("/")
  
def message(request):

  check = Message.objects.createMessage(
      request.POST['content'],
      request.session['user']
  )

  if not check["valid"]:
    for error in check["errors"]:
      messages.add_message(request, messages.ERROR, error)
      # context = {
      #   errors: 'errors'
      # }
    return redirect("/dashboard")
  else:
    request.session["user_id"] = check["user"].id
    messages.add_message(request, messages.SUCCESS, "Welcome, {}".format(request.POST["username"]))
    return redirect("/dashboard")
      
def comment(request):

  check = Comment.objects.createComment(
      request.POST['content'],
      request.session['user']
  )

  if not check["valid"]:
    for error in check["errors"]:
      messages.add_message(request, messages.ERROR, error)
      # context = {
      #   errors: 'errors'
      # }
    return redirect("/dashboard")
  else:
    messages.add_message(request, messages.SUCCESS, "Welcome, {}".format(request.POST["username"]))
    return redirect("/dashboard")

def logout(request):
  request.session.flush()
  return redirect('/')