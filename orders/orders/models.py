from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 255)
    mailing_address = models.TextField()
    email = models.CharField(max_length = 255)

class Order(models.Model):
    order_number = models.IntegerField()
    date = models.DateField()
