from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Brand, Product,Category
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model=User

        fields = ['username','password']
        extra_kwargs={'password':{'write_only':True}
        }

    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    discount  = serializers.IntegerField(source='get_item_price_after_discount')
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id','image','product_name','category','brand', 'color','rating','f_assured','price','discount_percentage','discount']


    def get_category(self,obj):

        return obj.category.category_name
    
    def get_brand(self,obj):

        return obj.brand.brand_name


class ProductAddSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['product_name','category','brand','image','color','f_assured','price','discount_percentage']


