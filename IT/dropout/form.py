from .models import people
from django.forms import ModelForm
from django import forms


class Editform_info(ModelForm):
    class Meta:
        model=people
        fields='__all__'

        widgets={
             'name':forms.TextInput(attrs={'class':'form-control'}),
              'place_of_birth':forms.TextInput(attrs={'class':'form-control'}),
              'company':forms.TextInput(attrs={'class':'form-control'}),



        }
