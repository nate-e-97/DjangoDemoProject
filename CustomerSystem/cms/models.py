from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=128) # Will include number, street, and any line 2 items
    city = models.CharField(max_length=32)
    zip = models.CharField(max_length=10) # Zip codes can be formed as either 00000 or 00000+0000
    state = models.CharField(max_length=2)