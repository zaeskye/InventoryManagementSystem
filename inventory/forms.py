from django import forms
from django.contrib.auth import authenticate
from .models import Product, Receiver

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productid','productname','supplier','productqty','productprice']


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ['receivername', 'receiverpositions', 'product', 'receiveqty', 'receivedate']