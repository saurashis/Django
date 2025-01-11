from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('EYEWEAR', 'Eyewear'),
        ('SUNGLASSES', 'Sunglasses'),
        ('READING_GLASS', 'Reading Glass'),
        ('OTHERS', 'Others'),
    ]

    MATERIAL_CHOICES = [
        ('PLASTIC', 'Plastic'),
        ('METAL', 'Metal'),
        ('COMPOSITE', 'Composite'),
    ]

    name = models.CharField(max_length=50, unique=True, help_text="Enter the product name")
    brand = models.CharField(max_length=50, help_text="Enter the brand name")
    description = models.TextField(help_text="Enter a description of the product")
    MRP = models.IntegerField(validators=[MinValueValidator(0)],default=0, help_text="Enter the maximum retail price")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='OTHERS', help_text="Select the product category")
    material = models.CharField(max_length=10, choices=MATERIAL_CHOICES, help_text="Select the material")
    lens = models.CharField(max_length=20, blank=True, help_text="Enter the lens type (if applicable)")
    stock = models.IntegerField(validators=[MinValueValidator(0)], help_text="Enter the stock quantity")
    discount = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)],default=0, help_text="Enter the discount percentage")
    date = models.DateField(default=datetime.date.today, help_text="Enter the date of addition")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    userprofile = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, help_text="Enter the first name")
    last_name = models.CharField(max_length=20, help_text="Enter the last name")
    email = models.EmailField(max_length=50, unique=True, help_text="Enter the email address")
    phone = models.CharField(max_length=10, help_text="Enter the phone number")
    address = models.TextField(help_text="Enter the address")
    second_address = models.TextField(blank=True,help_text="Enter the address")
    dob=models.DateField(null=True,help_text="Enter the date of birth")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.first_name + " " + self.last_name

class Order(models.Model):
    payment_choices = [

        ('CASH', 'Cash'),
        ('UPI', 'UPI')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField(validators=[MinValueValidator(0)],default=0, help_text="Enter the price")
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=1,help_text="Enter the quantity")
    date = models.DateField(default=datetime.date.today, help_text="Enter the date of order")
    Payment_mode=models.CharField(max_length=10,choices=payment_choices,default='CASH', help_text="Select the payment mode")


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name + " - " + self.product.name
    
class Feedback(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0, help_text="Enter the rating")
    comment=models.TextField(help_text="Enter the comment")
    date=models.DateField(default=datetime.date.today, help_text="Enter the date")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return (f"{self.order.customer.first_name}_{self.order.product.name}_Feedback_{self.rating}")


