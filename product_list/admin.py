from django.contrib import admin

from product_list.models import Brand, Category, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
