from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import FileField
from django.utils import timezone
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.FileField(upload_to='product/', null=True, verbose_name="")
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.product_name