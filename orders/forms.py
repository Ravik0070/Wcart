from django import forms
from django.forms import fields
from orders.models import Order

class OrderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','mobile','address','postal_code','city']
