from rest_framework import serializers
from .models import Product,Order,OrderItems
from optical_main import models
from django.db.models import Max


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    brand = serializers.CharField()
    description = serializers.CharField()
    MRP = serializers.IntegerField()
    def create(self, validated_data):
        try:
            return Product.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})    


class OrderItemsSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name')
    price=serializers.CharField(source='product.MRP')
    order_id=serializers.CharField(source='order.id')
    class Meta:
        model=OrderItems
        fields=['order_id','product_name','price','quentity']


class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemsSerializer(many=True)
    total_price=serializers.SerializerMethodField()
    def get_total_price(self,obj):
        total_price=obj.items.all()
        return sum(i.sub_total for i in total_price)
    class Meta:
        model=Order
        fields='__all__'
        extra_fields=['total_price','items']


class CustomeProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    MRP=serializers.IntegerField()
    last_ordered_date = serializers.SerializerMethodField()
    last_ordered_person = serializers.SerializerMethodField()
    def get_last_ordered_date(self, obj):
        order_item=OrderItems.objects.filter(product=obj).order_by('-order__date').first()
        if order_item:
            return order_item.order.date
    def get_last_ordered_person(self, obj):
        order_item=OrderItems.objects.filter(product=obj).order_by('-order__date').first()
        if order_item:
            return order_item.order.customar
        

class FeedbackListSerializer(serializers.ModelSerializer):
    name=serializers.CharField(source='order.customer.first_name')
    product=serializers.CharField(source='order.product.name')
    class Meta:
        model=models.Feedback
        fields=['id','name','rating','comment','product']
        #extra_fields=['name']

class FeedbackSerializer(serializers.ModelSerializer):
    name=serializers.CharField(source='order.customer.first_name',read_only=True)
    product=serializers.CharField(source='order.product.name',read_only=True)
        
    class Meta:
        model=models.Feedback
        fields=['name','rating','comment','product','date']
        #extra_fields=['name']
        def validate_rating(self,value):
            if value>5:
                raise serializers.ValidationError("Rating must be between 0 and 5.")
    

    
