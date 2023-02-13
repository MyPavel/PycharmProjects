from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description', 'name', 'quantity', 'category', 'price', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'products', ]


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['id', 'product', 'Order', ]
