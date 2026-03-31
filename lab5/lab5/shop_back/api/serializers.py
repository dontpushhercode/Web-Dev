from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if int(data.get('count'))==0:
            raise serializers.ValidationError("Product count can not be 0")
        if data.get('is_active')==False:
            raise serializers.ValidationError("Inactive product can not be created")
        return data
