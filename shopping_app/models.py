from django.db import models
from decimal import Decimal
#from payments import PurchasedItem
#from payments.models import BasePayment

# Create your models here.

class User_log(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class Product(models.Model):
    product = models.CharField(max_length=255)
    price = models.FloatField()
    image= models.ImageField(upload_to='img/',default='img/index.jpeg')

class Product1(models.Model):
    product = models.CharField(max_length=255)
    price = models.FloatField()
    image= models.ImageField(upload_to='img/',default='img/index.jpeg')

class Product2(models.Model):
    product = models.CharField(max_length=255)
    price = models.FloatField()
    image= models.ImageField(upload_to='img/',default='img/index.jpeg')

class Product3(models.Model):
    product = models.CharField(max_length=255)
    price = models.FloatField()
    image= models.ImageField(upload_to='img/',default='img/index.jpeg')


class Pur(models.Model):
    #2purchaser = models.ForeignKey(User_log,defau on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    rates = models.FloatField()
    nam = models.CharField(max_length=200)

