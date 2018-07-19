from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def createUser(self, form):
        flag = False
        errors = []

        new_user = self.create(email = 'email', password = 'password', username ='username')

        return(True, new_user)
    
    def login(self, form):
        flag = False
        errors = []

        called_user = User.manager.get(email=request.POST['email'])

        if called_user == null:
            errors.append("Username does not exist")
        if called_user.password != request.POST('password'):
            errors.append("Password incorrect")
        if flag:
            return (False, errors)
        
        return (True, called_user)

        # try:
        #     called_user = User.manager.get(email=data['email'])
        # except Exception:
        #     flag=True  
        #     errors.append(("Taken_User", "Username is incorrect/already taken"))
        #     return (False, errors)
        # if not bcrypt.checkpw(data['password'].encode(), called_user.password.encode()):
        #     flag= True
        #     errors.append(("password", "Password Incorrect"))

        # if flag:
        #     return (False, errors)

class MessageManager(models.Manager):
    def createMessage(self, form):

        flag = False
        errors = []

        if len(data['content']) < 1:
            flag = True
            errors.append(('first_name_length', "Your first name must be at least three characters long"))

        if flag:
            return (False, errors)
            
        # request.session id for poster?
        # User.manager.get(id=req.session['id'])??
        new_message = self.create(content = request.POST['content'], poster= data[''])
        return(True, new_message)

class CommentManager(models.Manager):
    def createComment(self, form):

        flag = False
        errors = []
        if len(data['content']) < 1:
            flag = True
            errors.append(('first_name_length', "Your first name must be at least three characters long"))

        if flag:
            return (False, errors)
            
        # request.session id for poster?
        new_comment = self.create(content = request.POST['content'], poster= data[''])
        return(True, new_comment)



class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()
    def __repr__(self): 
        return "My name is {} and I am a user.".format(self.username)

class Message(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = MessageManager()
    def __repr__(self): 
        return "I am a message created by {}.".format(self.poster)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = CommentManager()
    def __repr__(self): 
        return "I am a comment created by {}.".format(self.poster)
