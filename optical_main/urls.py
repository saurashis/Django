from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('home/',views.home,name='home'),
    path('login/',views.loginview,name='loginpage'),
    path('logout/',views.logoutview,name='logoutpage'),
    path('test/',views.print_request,name='test'),
    path('<int:id>', views.month_id, name='month_by_id'),
    path('cart/',views.cart_page,name='cart'),
    path('product/<int:id>',views.product,name='product_details'),
    path('order/',views.order,name='order'),
    path('hero/',views.hero,name='hero'),
]
