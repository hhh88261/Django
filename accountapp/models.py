from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    student_id = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)


class board(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)