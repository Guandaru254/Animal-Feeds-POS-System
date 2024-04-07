from django import forms
from .models import DairyMealBag
from .models import Client

class DairyMealBagForm(forms.ModelForm):
    class Meta:
        model = DairyMealBag
        fields = ['name', 'description', 'price', 'quantity_available']
        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phoneno', 'address']  # Define the fields you want to include in the form