from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
# Create your views here.


def index(request):
    return render(request, "wall/index.html")


def dashboard(request, first_name):
    context = {
        'first_name': first_name
    }
    # One for comments and one for messages
    # context = {"messages": Message.objects.all()}
    # context = {"authors": Comments.objects.all()}
    return render(request, "wall/dashboard.html", context)


def login(req):
    
    result = User.manager.login(req.POST)
    
    if result[0]:
        req.session['id'] = result[1].id
        # print req.session['id']
        return redirect('/dashboard')
    
    for message in result[1]:
        messages.error(req,message[1])
    
    return redirect('/')

def register(req):
    
    result = User.manager.createUser(req.POST)
    
    if result[0]:
        for key, message in result[1].iteritems():
            messages.error(req, message)
        return redirect('/')
    
    for key, message in result[1].iteritems():
        messages.error(req, message)
    
    return redirect('/')