from django.db import models



# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()
    
