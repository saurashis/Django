import os
import sys
import django
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optial_shop.settings')  # Replace with your project name
django.setup()

from optical_main.models import Product, Customer, Order, Feedback
from django.db.models import Count,F,Subquery,OuterRef,Avg,Sum,Max,Min,Q
from django.db import connection
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import random

p=Product.objects.filter(id__range=(5,15)).update(category='ETHNIC EYEWEAR')
print(p)
p=Product.objects.filter(id__range=(5,15))
for i in p:
    print(i.id,i.name,i.category)

#Product.objects.bulk_update(p,['MRP'])