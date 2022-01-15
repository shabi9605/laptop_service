from django import forms
from django.db.models import fields
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ('name','description','slug')


class ProductForm(forms.ModelForm):
    price_declare_date=DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Product
        fields = ('category','name','slug','image','price','price_declare_date','stock','description','is_available','created')