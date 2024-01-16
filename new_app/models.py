from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.auth import User
# Create your models here.
# class Users(models.Model):
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     email_address=models.EmailField(max_length=50)
#     password=models.CharField(max_length=20)
#     confirm_password=models.CharField(max_length=20)
#     status=models.BooleanField(default=False)

# class CustomUser(AbstractUser):
#     is_approved=models.BooleanField(default=False)

class Position(models.Model):
    name=models.CharField(max_length=50)
    max_vote=models.IntegerField()
    priority=models.IntegerField()

    # def __str__(self):

    #     return self.name

class Candidate(models.Model):
    fullname=models.CharField(max_length=50)
    bio=models.TextField()
    photo=models.ImageField(upload_to="candidates")
    # position=models.ForeignKey(Position,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.fullname
