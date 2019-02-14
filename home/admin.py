from django.contrib import admin
from .models import Product

my_model = [Product]
admin.site.register(my_model)

# Register your models here.