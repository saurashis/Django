from django.contrib import admin
from .models import Product, Type, Rating


# Register your models here.
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Rating)