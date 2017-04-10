from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Message


class MyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'message',]

    def save(self, commit=True):
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        inst = super().save()
        if message and name is None:
            raise ValueError('Massage is empty')
        else:
            return name, message
