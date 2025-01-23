import os
import sys
import django
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optial_shop.settings')  # Replace with your project name
django.setup()

from optical_main.models import Product, Customer, Order, Feedback
from django.db.models import Count,F,Subquery,OuterRef,Avg
from django.db import connection

order_list=Order.objects.filter(product=OuterRef('id')).order_by('-date')[:1].values('customer__first_name')
product_list=Product.objects.annotate(last_buy=Subquery(order_list))


for i in product_list:
    print(f"{i.name}__{i.last_buy}")
print('---------------------------------------------------')
print(connection.queries)
