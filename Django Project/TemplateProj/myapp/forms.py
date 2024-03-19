from django import forms
from .models import *


class contactForm(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'