import imp
from venv import create
from django.db import models


class Signup(models.Model):
    userId = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)