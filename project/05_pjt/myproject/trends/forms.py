from django import forms
from .models import Keyword

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ('name',)
        labels = {
            'name': '키워드',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
