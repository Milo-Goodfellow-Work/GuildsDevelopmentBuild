#Non project imports
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .forms import UserLoginCustomForm

#Project imports
from . import views

app_name='UserEntry'
urlpatterns = [
    path('Login/', auth_views.login, {'template_name': 'UserEntry/Login.html', 'authentication_form': UserLoginCustomForm }, name="Login"),
    path('Register/', views.UserRegistrationView, name="Register"),
    url('Activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.Activate, name='Activate'),
    path('ActivationSent/', views.ActivationSent, name="ActivationSent"),

]
