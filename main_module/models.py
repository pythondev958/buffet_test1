from django.db import models


class registration(models.Model):
    name = models.CharField(max_length=80)
    username= models.CharField(max_length=80)
    password= models.CharField(max_length=80)
    timestamp= models.CharField(max_length=80)
    email_id= models.CharField(max_length=80)

class login(models.Model):
    username = models.CharField(max_length=80)
    password= models.CharField(max_length=80)
