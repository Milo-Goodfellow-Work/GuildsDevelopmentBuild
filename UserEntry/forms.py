#Non project imports
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



#Project imports


#This form is present to allow for the presence of emails on the registration page for users
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Repeat password'})

class UserLoginCustomForm(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Username'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
