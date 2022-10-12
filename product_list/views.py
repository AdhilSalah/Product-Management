from rest_framework import viewsets,mixins
from rest_framework.permissions import AllowAny,IsAuthenticated
from product_list.serializers import BrandSerializer, CategorySerializer, ProductSerializer,ProductAddSerializer, UserSerializer
from .models import Product
from rest_framework import filters,generics
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib.auth.models import User
from rest_framework.response import Response

class RegisterView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
        
        
#for adding a Category
class CategoryView(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = CategorySerializer

#for adding brands
class BrandView(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = BrandSerializer

#custom Filter -------------------------------------
class ProductFilter(django_filters.FilterSet):
    product_price = django_filters.RangeFilter()
    class Meta:
        model = Product
        fields = ['price','rating']
#----------------------------------------------------

#product list and retrieve
class ProductView(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = {
    'category':['exact'],
    'brand':['exact'],
    'f_assured':['exact'],
    'price':['gte', 'lte'],
    'rating':['gte'],
    }
    filter_class = ProductFilter
    search_fields = ['product_name','category__category_name','brand__brand_name']

#product management
class ManageProductView(mixins.CreateModelMixin,
                
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
                
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductAddSerializer
    parser_classes = [MultiPartParser,FormParser]
    queryset = Product.objects.all()
        


