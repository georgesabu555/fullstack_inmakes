from django import forms
from .models import Cricketer

class CricketerForm(forms.ModelForm):
    class Meta:
        model=Cricketer
        fields=['name','desc','year','img']