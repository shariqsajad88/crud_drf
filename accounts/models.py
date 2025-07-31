from django.contrib.auth.models import User
from django.db import models

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.number

class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.address_line
