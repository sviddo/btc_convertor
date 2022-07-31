from django import forms

class AddEmailForm(forms.Form):
    email = forms.EmailField(label="Email: ", max_length=30)
    