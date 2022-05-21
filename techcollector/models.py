from audioop import reverse
from django.db import models
from django.urls import reverse

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length =100)
    specs = models.TextField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('techdetail',kwargs={'tech_id':self.id})   