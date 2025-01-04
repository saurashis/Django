from .models import Rating
from django import forms

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['rating','comments']

