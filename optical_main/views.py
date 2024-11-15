from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
# Create your views here.

def main(request):
    return HttpResponse('This main page')

def home(request):
    return redirect('main')  #This will redirect to main upon typing the /home

def about(request):
    return HttpResponse('This about page')

