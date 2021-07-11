from django.contrib.auth.models import User
from django.db import models

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = PhoneNumberField()
    address = models.CharField('Address', max_length=500)
    postcode = models.IntegerField()
    gender = models.CharField('Gender', max_length=50)
    dob = models.DateField()
    nationality = CountryField()

