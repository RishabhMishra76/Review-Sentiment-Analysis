from django import forms
from .models import date

class ReviewForm(forms.ModelForm):
    class Meta:
        model = date
        fields = ('name','c')