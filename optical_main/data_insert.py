# data_insert.py
import os
import sys
import django

# Add the project directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Set the Django settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optial_shop.settings')  # Replace with your project name
django.setup()

# Import the model
from optical_main.models import Product

# Example: Insert data into the Product model
p=Product.objects.get(id=1)
print(p.name)

