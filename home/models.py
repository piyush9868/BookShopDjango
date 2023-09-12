from django.db import models

#makemigrations: check for model changes and store it in the file
#migrate: apply pending changes created by makemigrate

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()