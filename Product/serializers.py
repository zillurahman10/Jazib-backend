# from rest_framework import serializers
# from . import models

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Product
#         fields = '__all__'

from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_url']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
