from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def createUser(self, form):
        flag = False
        errors = []
        # now= str(datetime.datetime.now())
        # if User.manager.filter(email = data['email']):
        #     flag = True
        #     errors.append(("used_email", "Email already registered."))
        #     return (False, collections.OrderedDict(errors))
        # if len(data['first_name'])<2:
        #     flag = True
        #     errors.append(('first_name_length', "Your first name must be at least three characters long"))
        # if len(data['last_name'])<2:
        #     flag = True
        #     errors.append(('last_name_length', "Your last name must be at least three characters long")) 
        
        # for char in range(len(data['first_name'])):
        #     if NAME_REGEX.match(data['first_name'][char]):
        #         errors.append(('first_name_number', "No non letters are allowed in first name"))
        #         flag = True
        #         break    
        # for char in range(len(data['last_name'])):
        #     if NAME_REGEX.match(data['last_name'][char]):
        #         errors.append(('last_name_number', "No non letters are allowed in last name"))
        #         flag = True
        #         break    
        # if not EMAIL_REGEX.match(data['email']):
        #     errors.append(('email', "Email Invalid."))
        #     flag = True
        # if not data['password']== data['confirm_password']:
        #     errors.append(('password', "Passwords do not match"))
        #     flag= True       
        # # if now > birthday:
        # #     errors.append(('date', "Birthday must be valid"))
        # #     flag= True
        # if flag:
        #     return (False, collections.OrderedDict(errors))

        new_user = self.create(email = 'email', password = 'password', username ='username')

        return(True, new_user)
    
    def login(self, form):
        flag = False
        errors = []
        try:
            called_user = User.manager.get(email=data['email'])
        except Exception:
            flag=True  
            errors.append(("Taken_User", "Username is incorrect/already taken"))
            return (False, errors)
        if not bcrypt.checkpw(data['password'].encode(), called_user.password.encode()):
            flag= True
            errors.append(("password", "Password Incorrect"))

        if flag:
            return (False, errors)
        return(True, called_user)

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
