from django.db import models

# Create your models here.

class User(models.Model):
    firstname=models.CharField(max_length=256)
    lastname=models.CharField(max_length=256)
    email=models.EmailField(max_length=254)

    def __str__(self):
        return self.firstname
