from django.db import models
from uuid import uuid3

#makemigrations: check for model changes and store it in the file
#migrate: apply pending changes created by makemigrate

# Create your models here.
class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

#book object
class Book(models.Model):
    title = models.CharField(max_length=100)
    ISBN_Number = models.CharField(max_length=13, primary_key=True, default="0-1339-5019-0")
    MRP_price = models.IntegerField()
    selling_Price = models.IntegerField()

