from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('<int:id>', views.month_id, name='month_by_id'),
    path('cart/',views.cart_page,name='cart'),
    path('home/<int:id>',views.product,name='product_details'),
]
