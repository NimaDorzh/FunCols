from django.db import models
"""Models view file"""

###Skeleton classes



##Addresses class
class Address(models.Model):
    # TODO: add list of addreesses
    zipcode = models.SmallIntegerField()
    country = models.CharField()
    city = models.CharField()




##Categories class
class Category(models.Model):
    category_name = models.CharField("")


#link to roles and available functions 
# TODO: HOW TO BETTER REALIZE?
class Function(models.Model):
    function_title = models.IntegerField()
    


##Items model class
class Item(models.Model):
    title = models.CharField(max_length=200)
    item_creation_date = models.DateTimeField("date created")
    item_description = models.TextField("")
    # TODO: link to Prices class
    price = models.FloatField()
    item_img_path = models.TextField("path to image")
    item_video_path = models.TextField("path to video")


##Price history class
class Price(models.Model):
    #price without discount
    typical_price = models.FloatField()
    #price with discount
    deal_price = models.FloatField()
    price_date = models.DateTimeField()
    #discount TODO: diff typical_price - deal_price

##Reviews class
class Review(models.Model):
    review_creation_date = models.DateTimeField()
    star = models.SmallIntegerField() 
    review_description = models.TextField()
    # TODO: how to store several images in one path?
    review_img_path = models.TextField("path to image")
    pros = models.CharField()
    cons = models.CharField()
    likes = models.IntegerField()

    
##Users role levels
class Role(models.Model):
    role_level = models.IntegerField()
    role_description = models.CharField()

#
class Store(models.Model):
    store_title = models.TextField()
    # TODO: what is better text path or img field?
    store_logo = models.ImageField()
    store_link = models.TextField()

##Users model class
class User(models.Model):
    name = models.CharField("")
    lastname = models.CharField("")
    email = models.CharField("")
    phone_number = models.CharField("")
    role_level = models.IntegerField()
    user_link = models.TextField()

###Features classes

# renames the instances of the model
# with their title name
def __str__(self):
    return self.title
    



