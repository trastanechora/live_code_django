from django import forms
from .models import Product

class PostForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ('product_name', 'price', 'photo', 'description')