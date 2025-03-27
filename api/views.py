from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from api.models import Product,Order,OrderItems
from optical_main.models import Feedback
from django.db.models import Sum,Max
from api.serializer import ProductSerializer,OrderSerializer,CustomeProductSerializer,OrderItemsSerializer,FeedbackListSerializer,FeedbackSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from api.Permission import IsCreator



'''class ProductAPIView(APIView):
    def get(self,request):
        p=Product.objects.filter(MRP__gt=100)
        serializer=ProductSerializer(p,many=True)
        return Response(serializer.data)'''
'''
@api_view(['GET','POST'])
@permission_classes([DjangoModelPermissions])
def ProductAPIView(request):
    if request.method=='GET':
        p=Product.objects.all()
        serializer=ProductSerializer(p,many=True)
        #print(f"csrf_token:{request.__dict__}")
        return Response(serializer.data)

    if request.method=='POST':
        p=request.data
        print('========request.data================',request.data)
        serializer=ProductSerializer(data=p)
        #print('========================',serializer.data)
        try:
            if serializer.is_valid():
                print('========serializer.is_valid()================',serializer.is_valid())
                print('========serializer.__dict__================',serializer.__dict__)
                serializer.save()
            #print(f"csrf_token:{request.__dict__}")
                return Response(serializer.data)
        except Exception as e:
            return Response({
                'error':str(e)
            })'''
        
class ProductAPIView(APIView):

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Product.objects.all()[:5]
    
    def get(self,request):
          
        p=self.get_queryset()
        serializer=ProductSerializer(p,many=True)
        #print(f"csrf_token:{request.__dict__}")
        return Response(serializer.data)
    
    def post(self,request):
        p=request.data
        serializer=ProductSerializer(data=p)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer)

       
   
class OrderObjects(ListAPIView):
    #queryset=Order.objects.all()
    def get_queryset(self):
        #user_name=str(self.request.user).split('_')[0].capitalize()
        return Order.objects.all()
    serializer_class=OrderSerializer



class OrderDetail(APIView):
    def get(self,request,id):
        user_name=str(request.user).split('_')[0].capitalize()
        #user_name=user_name.split('_')
        #user_name=(user_name[0].capitalize())
        order_item=Order.objects.filter(id=id)
        print(f"---------------{request.user}-------------------")

        serializer=OrderSerializer(order_item,many=True)
        return Response(serializer.data)


class FeedbacklistAPI(APIView):
    def get(self,request):
        f=Feedback.objects.all()
        serializer=FeedbackListSerializer(f,many=True)
        return Response(serializer.data)
    
class FeedbackAPI(APIView):
    permission_classes = [IsCreator]
    def get(self,request,id):
        f=Feedback.objects.get(id=id)
        serializer=FeedbackSerializer(f)
        return Response(serializer.data)
    
    def patch(self,request,id):
        f=Feedback.objects.get(id=id)
        self.check_object_permissions(request, f)
        data=request.data
        serializer=FeedbackSerializer(f,data=data,partial=True)
        if serializer.is_valid():
            if 'rating' in data:
                f.rating=data['rating']
                f.save()
        else:
            return Response({'error':'Value cant be ore than 5'})
        return Response(serializer.data)
    