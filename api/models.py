from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
   
    name = models.CharField(max_length=50, help_text="Enter the product name")
    brand = models.CharField(max_length=50, help_text="Enter the brand name")
    description = models.CharField(max_length=50,help_text="Enter a description of the product")
    MRP = models.IntegerField(default=0, help_text="Enter the maximum retail price")
    
class Order(models.Model):
    customar=models.CharField(max_length=30,default='User',null=True)
    date=models.DateField(default=datetime.date.today)

class OrderItems(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items',blank=True,default=None)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items',blank=True,default=None)
    quentity=models.PositiveSmallIntegerField(default=1)

    @property
    def sub_total(self):
        return (self.quentity*self.product.MRP)

