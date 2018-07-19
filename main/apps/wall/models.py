from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
   
    def login(self, email, password):

        errors = []
        
        if len(username) < 1:
            errors.append("username is required")
        elif not (username):
            errors.append("Invalid username")
        else:
            usersMatchingEmail = User.objects.filter(email=email)
            if len(usersMatchingUsername) == 0:
                errors.append("Unknown username")
        if len(password) < 1:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must be 8 characters or more")

        response = {
            "errors": errors,
            "valid": True,
            "username": None 
        }

        if len(errors) == 0:
            if password == usersMatchingUsername[0].password:
                response["username"] = usersMatchingUsername[0]
            else:
                errors.append("Incorrect password")

        if len(errors) > 0:
            response["errors"] = errors
            response["valid"] = False

        return response

    
    def register(self, email, password, username):

        errors = []

        if len(username) < 3:
            errors.append("Username must be 3 characters or more")
        if len(email) < 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email")
        else:
            usersMatchingEmail = User.objects.filter(email=email)
            if len(usersMatchingEmail) > 0:
                errors.append("Email already in use")

        if len(password) < 1:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must be 8 characters or more")

        response = {
            "errors": errors,
            "valid": True,
            "user": None 
        }

        if len(errors) > 0:
            response["valid"] = False
            response["errors"] = errors
        else:
            response["user"] = User.objects.create(
                username=username,
                email=email,
                password=password
            )
        return response


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
    objects = UserManager()
 

class Message(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()


class Comment(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
