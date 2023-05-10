from django.db import models

# Create your models here.

from django.db import models  
class Customer(models.Model):  
    cid = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "customer" 