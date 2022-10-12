from email.policy import default
from random import choices
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    category_name = models.CharField(max_length=225)

    def __str__(self):

        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=225)

    def __str__(self):
        return self.brand_name

        
class Product(models.Model):
    PRODUCT_COLOR = [
        ('Black', 'B'),
        ('White', 'W'),
    ]
    product_name = models.CharField(max_length = 225)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    color = models.CharField(max_length = 225,default='',choices= PRODUCT_COLOR)
    price = models.IntegerField()
    discount_percentage = models.IntegerField(blank = True,null = True)
    f_assured = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'product/images')
    rating = models.DecimalField(default=1,decimal_places = 1,max_digits = 2,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    
    def __str__(self):
        return self.name
    def get_item_price_after_discount(self):
        
        return self.price-(self.price * self.discount_percentage/100)
