import os
import sys
import django
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optial_shop.settings')  # Replace with your project name
django.setup()

from optical_main.models import Product, Customer, Order, Feedback
from django.db.models import Count,F,Subquery,OuterRef
from django.db import connection

top_customer=Order.objects.values('customer').annotate(customer_count=Count('customer')).order_by('-customer_count')[:1].values_list('customer__id',flat=True)
product_list=Order.objects.filter(customer__id__in=top_customer).values('product__name','quantity')

print(product_list)
print('---------------------------------------------------')
print(connection.queries)