from django.db import models
from users.models import User


class Resume(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    #insert cv