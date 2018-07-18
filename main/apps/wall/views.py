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
    
    # One for comments and one for messages
    # context = {"messages": Message.objects.all()}
    # context = {"authors": Comment.objects.all()}

    return render(request, "wall/dashboard.html", context)


def login(req):
    
    result = User.manager.login(req.POST)
    
    # if result[0]:
    #     req.session['id'] = result[1].id
    #     # print req.session['id']
    #     return redirect('/dashboard')
    
    # for message in result[1]:
    #     messages.error(req,message[1])
    
    return redirect('/')

def register(request):

    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']

    
    result = User.manager.createUser(request.POST)
    
    # if result[0]:
    #     for key, message in result[1].iteritems():
    #         messages.error(req, message)
    #     return redirect('/')
    
    # for key, message in result[1].iteritems():
    #     messages.error(req, message)
    
    return redirect('/')

def message(req):
    
    result = Message.manager.createMessage(req.POST)
    
    if result[0]:
        for key, message in result[1].iteritems():
            messages.error(req, message)
        return redirect('/dashboard')
    
    for key, message in result[1].iteritems():
        messages.error(req, message)
    
    return redirect('/')

def comment(req):
    
    result = Comment.manager.createComment(req.POST)
    
    if result[0]:
        for key, message in result[1].iteritems():
            messages.error(req, message)
        return redirect('/dashboard')
    
    for key, message in result[1].iteritems():
        messages.error(req, message)
    
    return redirect('/')

