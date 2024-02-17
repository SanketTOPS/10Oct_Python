from django import forms
from .models import *

class studform(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'
