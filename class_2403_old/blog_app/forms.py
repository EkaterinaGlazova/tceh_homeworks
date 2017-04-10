from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 1:
            raise ValidationError('Name is too short')
        return name

