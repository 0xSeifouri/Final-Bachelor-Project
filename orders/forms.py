from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'note']
        widgets = {
            'address': forms.Textarea(attrs={'rows':2}),
            'note': forms.Textarea(attrs={'rows':4}),

        }