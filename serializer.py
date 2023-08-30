from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = ["brand", "product_description", "is_manufacturer", "productid", "brandid", "ecolabel", "ecolabel_informations", "startdate", "enddate"]
