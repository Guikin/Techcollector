from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length =100)
    specs = models.TextField(max_length=255)
    price = models.IntegerField()