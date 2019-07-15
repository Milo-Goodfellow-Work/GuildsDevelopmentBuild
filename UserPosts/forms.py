from .models import UserPostModel
from django import forms

class UserPostModelForm(forms.ModelForm):
    class Meta():
        model = UserPostModel
        fields = ['PostBody']
        widgets = {
            'PostBody': forms.Textarea(attrs={'placeholder': 'Write about anything!'}),


        }
