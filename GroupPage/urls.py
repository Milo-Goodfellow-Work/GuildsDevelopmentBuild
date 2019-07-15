from django.urls import path
from . import views

app_name="GroupPage"
urlpatterns = [
    path('', views.GroupView, name='GroupNavigation')

]
