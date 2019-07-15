from django.urls import path
from . import views

app_name = 'UserSettings'
urlpatterns = [
    path('', views.SettingsLinkListView, name="UserSettings"),

]
