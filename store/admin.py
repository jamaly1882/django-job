from django.contrib import admin

# Register your models here.

from .models import Customer,Order,OrderItem, Product,ShippingAdress
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ShippingAdress)




# Register your models here.
