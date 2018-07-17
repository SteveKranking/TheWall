from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
NUM_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def uni_to_str(myDict):
    data = {}
    for key, val in myDict.iteritems():
        if key != 'csrfmiddlewaretoken':
            data[key] = str(val)
    return data


class UserManager(models.Manager):
    def makeUser(self, form):
        flag = False
        errors = {}
        data = uni_to_str(form)
        
        user = self.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))
        return (True, user)

    def userLogin(self, form):
        flag = False
        errors = {}
        data = uni_to_str(form)
        try:
            current_user = User.manager.get(email=data['email'])
        except Exception:
            errors['email'] = "That email does not exist in our records."
            return (False, errors)
        if not bcrypt.checkpw(data['password'].encode(), current_user.password.encode()):
            flag = True
            errors['password'] = "That password doesn't match the one we've got..."
        if flag:
            return (False, errors)
        return (True, current_user)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()