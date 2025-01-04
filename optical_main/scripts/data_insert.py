# data_insert.py
import os
import sys
import django
from django.db import connection,models
from django.db.models import base

# Add the project directory to the system path

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Set the Django settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optial_shop.settings')  # Replace with your project name
django.setup()

# Import the model
from optical_main.models import Product
from optical_main.models import Type
from django.db.models import Avg, Max,Count,Sum,F,CharField,Value
from django.db.models.functions import Concat
from django.db import connection

type_list=['Spectacles', 'Reading Glass', 'Riding Glass', 'Protective Glass', 'Sunglasses']

catalog = {
    1: {
        "eyewear_name": "Urban Classic Spectacles",
        "type": "Spectacles",
        "description": "A lightweight metal-framed design that combines simplicity with elegance. Perfect for daily wear at work or casual outings, ensuring lasting comfort and style.",
        "price": 2499,
        "available_lens_options": ["Clear", "Blue-Light Blocking", "Anti-Glare", "Photochromic"]
    },
    2: {
        "eyewear_name": "Sleek Round Frames",
        "type": "Spectacles",
        "description": "Vintage-inspired round frames that add a timeless, intellectual appeal. Made from premium acetate, they are both lightweight and durable for long-term use.",
        "price": 2899,
        "available_lens_options": ["Clear", "Blue-Light Blocking", "High-Index", "Anti-Glare"]
    },
    3: {
        "eyewear_name": "Luxe Rectangle Frames",
        "type": "Spectacles",
        "description": "A minimalist, rectangular frame ideal for professionals. Crafted with lightweight metal, these frames are both stylish and practical for all-day wear.",
        "price": 3399,
        "available_lens_options": ["Clear", "High-Index", "Photochromic", "Blue-Light Blocking"]
    },
    4: {
        "eyewear_name": "Classic Reading Glasses",
        "type": "Reading Glass",
        "description": "Designed for avid readers, these glasses feature a lightweight frame and high-quality lenses to reduce eye strain during long reading sessions.",
        "price": 1799,
        "available_lens_options": ["Clear", "Anti-Glare"]
    },
    5: {
        "eyewear_name": "Adjustable Focus Reading Glasses",
        "type": "Reading Glass",
        "description": "Equipped with adjustable focus lenses, these glasses are perfect for users with varying focal needs, providing clear vision for all distances.",
        "price": 2199,
        "available_lens_options": ["Clear", "Anti-Reflective"]
    },
    6: {
        "eyewear_name": "Polarized Riding Glasses",
        "type": "Riding Glass",
        "description": "Durable and stylish riding glasses with polarized lenses that reduce glare and enhance visibility during outdoor adventures.",
        "price": 3299,
        "available_lens_options": ["Polarized", "UV Protection"]
    },
    7: {
        "eyewear_name": "Wraparound Riding Goggles",
        "type": "Riding Glass",
        "description": "Designed for motorcyclists, these wraparound goggles offer a snug fit and superior protection from dust and wind.",
        "price": 2999,
        "available_lens_options": ["Anti-Fog", "UV Protection"]
    },
    8: {
        "eyewear_name": "Safety Protective Glasses",
        "type": "Protective Glass",
        "description": "Essential safety glasses for industrial and lab work, featuring impact-resistant lenses and a comfortable fit for all-day wear.",
        "price": 1499,
        "available_lens_options": ["Clear", "Scratch-Resistant"]
    },
    9: {
        "eyewear_name": "Anti-Fog Safety Goggles",
        "type": "Protective Glass",
        "description": "Heavy-duty goggles with anti-fog lenses, perfect for medical professionals or anyone working in high-humidity environments.",
        "price": 1899,
        "available_lens_options": ["Anti-Fog", "UV Protection"]
    },
    10: {
        "eyewear_name": "Polarized Aviator Sunglasses",
        "type": "Sunglasses",
        "description": "Timeless aviator sunglasses with polarized lenses to reduce glare, offering both style and excellent UV protection.",
        "price": 3499,
        "available_lens_options": ["Polarized", "UV Protection"]
    },
    11: {
        "eyewear_name": "Sporty Sunglasses",
        "type": "Sunglasses",
        "description": "Lightweight, sporty design perfect for outdoor activities. Features shatterproof lenses and maximum UV protection.",
        "price": 2499,
        "available_lens_options": ["Polarized", "Anti-Reflective"]
    },
    12: {
        "eyewear_name": "Blue-Light Blocking Glasses",
        "type": "Spectacles",
        "description": "Modern frames with blue-light blocking lenses to reduce eye strain from prolonged screen exposure.",
        "price": 1999,
        "available_lens_options": ["Blue-Light Blocking", "Anti-Glare"]
    },
    13: {
        "eyewear_name": "Photochromic Sunglasses",
        "type": "Sunglasses",
        "description": "Lenses that automatically adjust to changing light conditions, offering convenience and UV protection.",
        "price": 2999,
        "available_lens_options": ["Photochromic", "UV Protection"]
    },
    14: {
        "eyewear_name": "Retro Round Glasses",
        "type": "Spectacles",
        "description": "Retro-inspired frames that blend vintage charm with modern design. Ideal for anyone looking to make a bold style statement.",
        "price": 2799,
        "available_lens_options": ["Clear", "High-Index"]
    },
    15: {
        "eyewear_name": "Gaming Glasses",
        "type": "Protective Glass",
        "description": "Specially designed glasses for gamers with blue-light blocking and anti-glare lenses to reduce eye fatigue.",
        "price": 1999,
        "available_lens_options": ["Blue-Light Blocking", "Anti-Glare"]
    },
    16: {
        "eyewear_name": "Pilot Goggles",
        "type": "Riding Glass",
        "description": "Vintage-inspired goggles perfect for pilots and bikers, offering comfort and wind protection.",
        "price": 2799,
        "available_lens_options": ["Anti-Reflective", "UV Protection"]
    },
    17: {
        "eyewear_name": "Minimalist Square Frames",
        "type": "Spectacles",
        "description": "Clean, square-shaped frames that suit any face shape. Lightweight and designed for comfort and style.",
        "price": 2199,
        "available_lens_options": ["Clear", "Anti-Glare"]
    },
    18: {
        "eyewear_name": "Cycling Glasses",
        "type": "Riding Glass",
        "description": "Ergonomic frames designed for cyclists, with shatterproof and UV-protective lenses for enhanced performance.",
        "price": 3199,
        "available_lens_options": ["Polarized", "UV Protection"]
    },
    19: {
        "eyewear_name": "Industrial Safety Glasses",
        "type": "Protective Glass",
        "description": "Heavy-duty safety glasses with side shields and impact-resistant lenses for optimal protection.",
        "price": 1599,
        "available_lens_options": ["Clear", "Scratch-Resistant"]
    },
    20: {
        "eyewear_name": "Premium Cat-Eye Sunglasses",
        "type": "Sunglasses",
        "description": "Chic, cat-eye frames with polarized lenses that offer a bold fashion statement and superior UV protection.",
        "price": 3799,
        "available_lens_options": ["Polarized", "Anti-Reflective"]
    }
}


#t=Type.objects.values_list('name',flat=True)
#['Spectacles', 'Reading Glass', 'Riding Glass', 'Protective Glass', 'Sunglasses']

t=Product.objects.values('type__name').annotate(pr=Count('id'))
for i in t:
    print(i)