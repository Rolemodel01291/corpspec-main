from django.db import models

# Create your models here.
class Client(models.Model):
    uuid = models.CharField('Uuid', max_length=50)
    name = models.CharField('Client Name', max_length=300)
    address = models.CharField('Address', max_length=500)
    postcode = models.IntegerField()