from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

#when creating or editing models, we must migrate by - python3 manage.py makemigrations and python3 manage.py migrate

#test in shell by - from appname.models import model name
    #In the test shell, we call the model by name and press "enter". We will then be show information about it: class 'appname.models.model. We can then type modelname.objects.all() to see a query set of that model.

class Station(models.Model):
    stid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=100, default=" ")
    staddress = models.CharField(max_length=100)
    stcity = models.CharField(max_length=50)
    ststate = models.CharField(max_length=50)
    stpost = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
  

    def __str__(self):
        return self.stname
    
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=100)

    def __str__(self):
        return self.username