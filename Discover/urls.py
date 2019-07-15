#Non project imports
from django.urls import path

#Project imports
from . import views

app_name="Discover"
urlpatterns = [
    path('', views.Discover, name="DiscoverPage")

]
