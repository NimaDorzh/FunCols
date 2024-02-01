from django.db import models
"""Models view file"""

###Skeleton classes

##Users model class
class Users(models.Model):
    name = models.CharField("")
    lastname = models.CharField("")
    email = models.CharField("")
    phone_number = models.CharField("")
    role_level = models.IntegerField()
    user_link = models.TextField()
    #
##Users role levels
class Roles(models.Model):
    #role_level = models.IntegerField()
    role_description = models.CharField()


#link to roles and available functions 
# TODO: HOW TO BETTER REALIZE?
class Functions(models.Model):
    function_title = models.IntegerField()
    

#
class Stores(models.Model):
    store_title = models.TextField()
    # TODO: what is better text path or img field?
    store_logo = models.ImageField()
    store_link = models.TextField()



##Items model class
class Items(models.Model):
    title = models.CharField(max_length=200)
    item_creation_date = models.DateTimeField("date created")
    item_description = models.TextField("")
    # TODO: link to Prices class
    price = models.FloatField()
    item_img_path = models.TextField("path to image")
    item_video_path = models.TextField("path to video")

##Price history class
class Prices(models.Model):
    #price without discount
    typical_price = models.FloatField()
    #price with discount
    deal_price = models.FloatField()
    price_date = models.DateTimeField()
    #discount TODO: diff typical_price - deal_price

##Reviews class
class Reviews(models.Model):
    review_creation_date = models.DateTimeField()
    star = models.SmallIntegerField() 
    review_description = models.TextField()
    # TODO: how to store several images in one path?
    review_img_path = models.TextField("path to image")
    pros = models.CharField()
    cons = models.CharField()
    likes = models.IntegerField()

##Addresses class
class Addresses(models.Model):
    # TODO: add list of addreesses
    zipcode = models.SmallIntegerField()
    country = models.CharField()
    city = models.CharField()


##Categories class
class Categories(models.Model):
    category_name = models.CharField("")



###Features classes
    



