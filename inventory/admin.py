from django.contrib import admin
from .models import Supplier, Product, Receiver

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Receiver)