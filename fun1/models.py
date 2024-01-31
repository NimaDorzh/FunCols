from django.db import models
"""Models view file"""
# Create your models here.

###Skeleton classes
##Items model class
class Items(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")
    description = models.TextField("")

    # link to Prices class
    price = models.FloatField()
    img_path = models.TextField("path to image")
    video_path = models.TextField("path to video")


##Users model class
class Users(models.Model):
    name = models.CharField("")
    lastname = models.CharField("")
    email = models.CharField("")
    phone_number = models.CharField("")
    role = models.IntegerField()
    #

class Roles(models.Model):
    level = models.IntegerField()
    role_description = models.CharField()

##Price history class
class Prices(models.Model):
    current_price = models.FloatField()


###Features classes


