from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.urls import reverse
import os
# Create your views here.



dir=  {
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
        "eyewear_name": "Elegance Cat-Eye Glasses",
        "type": "Spectacles",
        "description": "Designed for the modern woman, these cat-eye glasses exude elegance. The bold frames add a chic touch, making them perfect for formal and casual settings alike.",
        "price": 3099,
        "available_lens_options": ["Clear", "Anti-Glare", "Blue-Light Blocking", "Scratch-Resistant"]
    },
    5: {
        "eyewear_name": "Retro Oval Glasses",
        "type": "Spectacles",
        "description": "Bring back vintage vibes with these lightweight, retro-inspired oval frames. Comfortable and stylish, they’re a great choice for casual wear.",
        "price": 2599,
        "available_lens_options": ["Clear", "Anti-Glare", "High-Index", "Blue-Light Blocking"]
    },
    6: {
        "eyewear_name": "PureVision Rimless Glasses",
        "type": "Spectacles",
        "description": "These rimless glasses are the epitome of sophistication and simplicity. Designed for professionals, they are ultra-lightweight and almost invisible for a sleek, modern look.",
        "price": 3799,
        "available_lens_options": ["Clear", "High-Index", "Anti-Glare", "Blue-Light Blocking"]
    },
    7: {
        "eyewear_name": "Bold Rectangle Glasses",
        "type": "Spectacles",
        "description": "Durable yet lightweight rectangular frames designed for durability and long-lasting comfort. Perfect for everyday use, blending utility and fashion effortlessly.",
        "price": 2999,
        "available_lens_options": ["Clear", "Anti-Glare", "Blue-Light Blocking", "Photochromic"]
    },
    8: {
        "eyewear_name": "Fusion Dual-Tone Glasses",
        "type": "Spectacles",
        "description": "Trendy dual-tone frames designed for those who want to add a pop of color to their daily style. Lightweight and comfortable for all-day wear.",
        "price": 2799,
        "available_lens_options": ["Clear", "Blue-Light Blocking", "Anti-Glare", "Scratch-Resistant"]
    },
    9: {
        "eyewear_name": "SmartFit Reading Glasses",
        "type": "Spectacles",
        "description": "These lightweight reading glasses are perfect for long hours of study or work. Designed to reduce eye strain, they provide sharp clarity and unmatched comfort.",
        "price": 1999,
        "available_lens_options": ["Reading", "Blue-Light Blocking", "Anti-Glare"]
    },
    10: {
        "eyewear_name": "Minimalist Titanium Frames",
        "type": "Spectacles",
        "description": "A blend of durability and style, these titanium frames are designed for professionals who value a lightweight and sleek appearance.",
        "price": 4099,
        "available_lens_options": ["Clear", "High-Index", "Anti-Glare", "Photochromic"]
    },
    11: {
        "eyewear_name": "Bold Wayfarer Sunglasses",
        "type": "Sunglasses",
        "description": "Featuring a matte-finish and classic wayfarer design, these sunglasses provide excellent UV protection and a bold look perfect for outdoor adventures.",
        "price": 3199,
        "available_lens_options": ["UV Protection", "Polarized", "Gradient"]
    },
    12: {
        "eyewear_name": "Aviator Sunglasses Pro",
        "type": "Sunglasses",
        "description": "Iconic aviators with mirrored lenses to block glare and offer full UV protection. Lightweight and durable, they are perfect for sunny days or long drives.",
        "price": 4299,
        "available_lens_options": ["Polarized", "UV Protection", "Mirror Coated"]
    },
    13: {
        "eyewear_name": "Polar Performance Shades",
        "type": "Sunglasses",
        "description": "Designed for adventurers, these polarized performance sunglasses reduce glare and offer superior clarity, making them ideal for hiking or water activities.",
        "price": 3999,
        "available_lens_options": ["Polarized", "UV Protection", "Scratch-Resistant"]
    },
    14: {
        "eyewear_name": "Sunset Gradient Shades",
        "type": "Sunglasses",
        "description": "Featuring gradient-tinted lenses and a sleek metal frame, these sunglasses are perfect for sunny afternoons. A stylish and functional accessory for any occasion.",
        "price": 3299,
        "available_lens_options": ["Gradient", "UV Protection", "Scratch-Resistant"]
    },
    15: {
        "eyewear_name": "Active Sport Sunglasses",
        "type": "Sunglasses",
        "description": "Built for performance, these wrap-around sunglasses offer impact-resistant lenses and UV protection. Perfect for outdoor sports and high-action adventures.",
        "price": 4699,
        "available_lens_options": ["Polarized", "UV Protection", "Scratch-Resistant"]
    },
    16: {
        "eyewear_name": "Luxe Glam Round Shades",
        "type": "Sunglasses",
        "description": "A glamorous addition to your collection, these round mirrored sunglasses combine luxury with functionality, offering full UV protection for sunny days out.",
        "price": 5199,
        "available_lens_options": ["Mirror Coated", "Gradient", "Polarized"]
    },
    17: {
        "eyewear_name": "Bold Oversized Sunglasses",
        "type": "Sunglasses",
        "description": "Make a statement with oversized frames and gradient lenses. These sunglasses are a perfect mix of fashion and function for the modern-day trendsetter.",
        "price": 4499,
        "available_lens_options": ["Gradient", "UV Protection", "Polarized"]
    },
    18: {
        "eyewear_name": "SportShield Sunglasses",
        "type": "Sunglasses",
        "description": "Wrap-around sunglasses designed for athletes. With their scratch-resistant polarized lenses, they deliver unmatched clarity and protection.",
        "price": 5499,
        "available_lens_options": ["Polarized", "UV Protection", "Scratch-Resistant"]
    },
    19: {
        "eyewear_name": "Mirrored Aviator Shades",
        "type": "Sunglasses",
        "description": "A bold and modern take on the classic aviators. Featuring reflective mirror lenses, these shades offer style, UV protection, and exceptional comfort.",
        "price": 4999,
        "available_lens_options": ["Mirror Coated", "UV Protection", "Polarized"]
    },
    20: {
        "eyewear_name": "Urban Edge Square Shades",
        "type": "Sunglasses",
        "description": "Sharp and contemporary square sunglasses that redefine casual style. Lightweight and designed for maximum comfort, perfect for everyday use.",
        "price": 3299,
        "available_lens_options": ["UV Protection", "Gradient", "Polarized"]
    }
}

def print_request(request):
    res=(request.POST)
    #res=dir(res)
    print(res)
    return HttpResponse(request.user)

def month_id(request,id):
    l=list(dir.keys())
    url = reverse('months', args=[l[id-1]])
    print(url)
    return redirect(url)

def product(request,id):
    product=dir[id]
    return render(request,'Optical_main/product.html',{
        'product':product})

def main(request):
    #eye_ware=list(dir.keys())
    #eye_ware_list={'names':eye_ware}
    return render(request,'Optical_main/home.html',{'dir':dir})  

def home(request):
    return render(request,'Optical_main/home.html')  

def cart_page(request):
    return render(request,'Optical_main/cart-item.html')

def about(request):
    return render(request,'Optical_main/test.html') 

    