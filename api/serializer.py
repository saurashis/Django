from rest_framework import serializers
from .models import Product,Order,OrderItems
from django.db.models import Max

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name')
    class Meta:
        model=OrderItems
        fields=['id','product_name','quentity']

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemsSerializer(many=True)

    #total_price=serializers.SerializerMethodField()

    def get_total_price(self,obj):
        items=obj.items.all()
        return sum(item.sub_total for item in items)
    
    class Meta:
        model=Order
        fields=['id','customar','items','date']


class CustomeProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    MRP=serializers.IntegerField()
   
    last_ordered_date = serializers.SerializerMethodField()
    last_ordered_person = serializers.SerializerMethodField()

    def get_last_ordered_date(self, obj):
        order_item=OrderItems.objects.filter(product=obj).order_by('-order__date').first()
        #last_or    OrderItems.objects.filter(product=obj).order_by('-order__date').first()
        if order_item:
            return order_item.order.date
    def get_last_ordered_person(self, obj):
        order_item=OrderItems.objects.filter(product=obj).order_by('-order__date').first()
        #last_or    OrderItems.objects.filter(product=obj).order_by('-order__date').first()
        if order_item:
            return order_item.order.customar

    
