from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):

    location = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'ex) 제주도'
            }
        )
    )
    
    plan = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder' : 'ex) 슉.슈슉.'
            }
        )
    )
    
    start_date = forms.CharField(
        widget = forms.DateInput(
            attrs={
                'placeholder' : 'ex) 2022-02-22'
            }
        )
    )
    end_date = forms.CharField(
        widget = forms.DateInput(
            attrs={
                'placeholder' : 'ex) 2022-02-22'
            }
        )
    )

    class Meta:
        model = Travel
        fields = '__all__'