from django import forms
from .models import CartItem

class CartForm(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = [
            'quantity',
        ]

        labels = {
            'quantity': '주문수량',
        }