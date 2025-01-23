from django.urls import path
from .views import product_api,OrderObjects,OrderDetail

urlpatterns = [
    path('product/', product_api),
    path('order/', OrderObjects.as_view()),
    path('order/<int:id>',OrderDetail.as_view()),
]
