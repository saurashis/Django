from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from api.models import Product,Order,OrderItems
from django.db.models import Sum,Max
from api.serializer import ProductSerializer,OrderSerializer,CustomeProductSerializer,OrderItemsSerializer

@api_view(['GET'])
def product_api(request):
    print((request._user))
    product = Product.objects.all()
    serializer = CustomeProductSerializer(product,many=True)
    return Response(serializer.data)
   
class OrderObjects(ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


class OrderDetail(RetrieveAPIView):
    queryset=OrderItems.objects.all()
    serializer_class=OrderItemsSerializer
    lookup_field='id'

# Create your views here.
