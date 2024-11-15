from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('<month>',views.months,name='months'),
]
