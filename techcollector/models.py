from audioop import reverse
from pyexpat import model
from django.db import models
from django.forms import CharField
from django.urls import reverse

# Create your models here.

class Perks(models.Model):
    name=models.CharField(max_length=100)
    value=models.CharField(max_length=100)

    def __str__(self):
        return self.name 

    # def get_absolute_url(self):
    #     return reverse('perkdetail',kwargs={'tech_id':self.id})     


class Tech(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length =100)
    specs = models.TextField(max_length=255)
    price = models.IntegerField()
    perk = models.ManyToManyField(Perks)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('techdetail',kwargs={'tech_id':self.id})

    class Meta:
        ordering = ['id']    



class Providers(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    stock=models.BooleanField()

    def __str__(self):
        return self.name
    tech= models.ForeignKey(Tech,on_delete=models.CASCADE)    

    class Meta:
        ordering = ['-id']


 