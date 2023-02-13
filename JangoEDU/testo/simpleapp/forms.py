from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = [
           'name',
           'description',
           'quantity',
           'category',
           'price',
       ]
