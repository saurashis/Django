# data_insert.py
import os
import sys
import django
from django.db import connection,models
from django.db.models import base
import random

import datetime

# Add the project directory to the system path

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Set the Django settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optial_shop.settings')  # Replace with your project name
django.setup()

from django.contrib.auth.models import User

names_data =[
    "Vintage Wayfarer Glasses",
    "Minimalist Clear Frames",
    "Mirrored Lens Sunglasses",
    "Luxury Metal Frame Glasses",
    "Smart Bluetooth Glasses",
    "Trendy Cat-Eye Eyewear",
    "Eco-Friendly Wooden Frames",
    "UV Protection Sunglasses",
    "Colorful Kids Eyeglasses",
    "Fashionable Rimless Glasses",
    "High-Definition Lenses",
    "Designer Optical Frames",
    "Polarized Driving Glasses",
    "Fashion Forward Oval Frames",
    "Sleek Titanium Glasses",
    "Waterproof Sports Eyewear",
    "Oversized Shield Sunglasses",
    "Classic Black Metal Eyeglasses",
    "Premium High-Index Lenses",
    "Luxury Designer Sunglasses",
    "Chic Transparent Frames",
    "Reversible Flip-Up Glasses",
    "Luxury Gradient Sunglasses",
    "Sporty Wraparound Sunglasses",
    "Bohemian Round Eyewear",
    "Bold Geometric Glasses",
    "Wooden Temple Glasses",
    "Classic Gold-Frame Sunglasses",
    "Unisex Minimalist Glasses",
    "Street Style Sunglasses",
    "Lightweight Aluminium Frames",
    "Round Retro Optical Glasses",
    "Dual-Tone Modern Eyeglasses",
    "Futuristic Full-Rim Frames",
    "Vintage Tortoise Shell Glasses",
    "Matte Black Frame Sunglasses"
]

brands_data = random.choice([
    "Luxora Optics",
    "Visionary Shades",
    "ClearView Eyewear",
    "Sunbeam Spectacles",
    "BoldFrame",
    "PureLens",
    "UrbanOptic",
    "Sunglo Eyewear",
    "VividEyes",
    "Eclat Glasses"
])

description_data="A cool pair of sunglasses"
mrp_data=random.randrange(900,2000)
catagory_data = random.choice(['EYEWEAR', 'SUNGLASSES', 'READING_GLASS', 'OTHERS'])
material_data = random.choice(['PLASTIC', 'METAL', 'COMPOSITE'])
lens_data=random.choice(['Clear', 'High-Index', 'Photochromic', 'Blue-Light Blocking'])
stock_data=random.randrange(10,100)
discount_data=random.randrange(0,50)
date_data=datetime.date.today()

first_names = [
    "Arjun",
    "Priya",
    "Ravi",
    "Sneha",
    "Rahul",
    "Ananya",
    "Vikram",
    "Kavya",
    "Amit",
    "Neha",
    "Siddharth",
    "Isha",
    "Rohit",
    "Pooja",
    "Karan",
    "Meera",
    "Akash",
    "Shreya",
    "Manish",
    "Tanya"
]


last_names = [
    "Sharma",
    "Verma",
    "Gupta",
    "Patel",
    "Singh",
    "Kumar",
    "Das",
    "Iyer",
    "Chopra",
    "Nair",
    "Malhotra",
    "Reddy",
    "Joshi",
    "Mehta",
    "Agarwal",
    "Jain",
    "Chaudhary",
    "Pandey",
    "Yadav",
    "Bhattacharya"
]
last_names = [
    "Sharma",
    "Verma",
    "Gupta",
    "Patel",
    "Singh",
    "Kumar",
    "Das",
    "Iyer",
    "Chopra",
    "Nair",
    "Malhotra",
    "Reddy",
    "Joshi",
    "Mehta",
    "Agarwal",
    "Jain",
    "Chaudhary",
    "Pandey",
    "Yadav",
    "Bhattacharya"
]



from optical_main.models import Product, Customer,Order,Feedback
from django.contrib.auth.models import User
from django.db.models import Count,F,Subquery,OuterRef,Avg,Sum,Max,Min,Q
from django.db import transaction

def user_insert():
    for i in range(20):
        user = User.objects.create_user(
            username=f"{first_names[i].lower()}_{last_names[i].lower()}",
            email=f"{first_names[i].lower()}{last_names[i].lower()}@example.com",
            password="password123"

        )
        user.save()
        print(f"User {first_names[i]} inserted successfully")

def customer_insert():
    for i in range(20):
        customer = Customer.objects.create(
            userprofile=User.objects.get(id=i+2),
            first_name=first_names[i],
            last_name=last_names[i],
            email=f"{first_names[i].lower()}{last_names[i].lower()}@example.com",
            phone=f"9{random.randint(100000000, 999999999)}",
            address=f"{random.randint(1, 999)}, {random.choice(['1st', '2nd', '3rd', '4th'])} Main, {random.choice(['1st', '2nd', '3rd', '4th'])} Block, {random.choice(['Koramangala', 'Indiranagar', 'HSR Layout', 'JP Nagar'])}, Bangalore",
            dob=datetime.date(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28))
        )
        customer.save()
        print(f"Customer {first_names[i]} inserted successfully")

def product_insert():
    product = Product.objects.create(
        name=names_data,
        brand=brands_data,
        description=description_data,
        MRP=mrp_data,
        category=catagory_data,
        material=material_data,
        lens=lens_data,
        stock=stock_data,
        discount=discount_data,
        date=date_data
    )
    product.save()
    print(f"Product inserted successfully")

def order_create(n):
    for i in range(n):
        product_id=random.randint(1, 40)
        order = Order.objects.create(
            customer=Customer.objects.get(id=random.randint(2, 20)),
            product=Product.objects.get(id=product_id),
            price=Product.objects.get(id=product_id).MRP,
            quantity=random.randint(1, 5),
            date=datetime.date(random.randint(2023, 2024), random.randint(1, 12), random.randint(1, 28)),
            Payment_mode=random.choice(['CASH', 'UPI'])
        )
        order.save()
        print(f"Order {i+1} inserted successfully")

def feedback_create(n):
    for i in range(n):
        feedback = Feedback.objects.create(

        order=Order.objects.get(id=i+1),    
        rating=random.randint(1, 5),
        comment = 'This product is fabulous',
        date=Order.objects.get(id=i+1).date+ datetime.timedelta(days=random.randint(1, 10)))

        feedback.save()
        print(f"Feedback {i+1} inserted successfully")



    
