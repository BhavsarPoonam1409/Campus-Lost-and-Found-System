from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'item_name',
            'description',
            'category',
            'location',
            'item_date',
            'contact_details',
        ]

        widgets = {
            'item_name': forms.TextInput(attrs={
                'placeholder': 'Enter item name'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the item',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter campus location'
            }),
            'item_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'contact_details': forms.TextInput(attrs={
                'placeholder': 'Phone number or email'
            }),
        }

