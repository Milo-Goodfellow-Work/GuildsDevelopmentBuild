from django.urls import path

from . import views

app_name = "FullSearch"
urlpatterns = [
    path('', views.SearchView, name="Search")

]
