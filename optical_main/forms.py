
from django import forms

from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(label="Please enter User ID", max_length=100)
    password = forms.CharField(label="Password")

