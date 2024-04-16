from django import forms
from .models import travels

class TravelForm(forms.ModelForm):
    class Meta:
        model = travels
        fields = '__all__'