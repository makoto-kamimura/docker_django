from django.contrib import admin

from .models import Product, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display=('pk','name', 'price')

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('pk','created_date', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
