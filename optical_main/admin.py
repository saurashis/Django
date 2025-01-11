from django.contrib import admin
from .models import Product, Customer, Order, Feedback

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','MRP','brand','category','stock','discount','date']

    list_filter = ('brand', 'category')
    search_fields = ('id','name')


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Customer)   
admin.site.register(Order)
admin.site.register(Feedback)
