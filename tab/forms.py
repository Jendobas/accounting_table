from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('art', 'model', 'color', 'size', 'structure', 'shipment', 'count', 'seller', 'date_name')


class Filter(forms.Form):
    filter_seller = forms.ChoiceField(choices=(
        ('GUM', 'GUM'),
        ('SLAVUTINY', 'SLAVUTINY'),
        ('SALON', 'SALON')
    ))


class FilterDate(forms.Form):
    filter_date = forms.ChoiceField(choices=(
        ('WEEK', 'WEEK'),
        ('MONTH', 'MONTH'),
    ))
