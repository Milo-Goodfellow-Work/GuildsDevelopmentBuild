from django.forms import ModelForm
from django import forms
from .models import Message

class ChatModelForm(ModelForm):
    class Meta:
        model = Message
        fields=['MessageBody']
        widgets = {
        'MessageBody' : forms.TextInput(attrs={'placeholder': 'Message your group!'}),

        }
