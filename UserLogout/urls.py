from django.urls import path

from . import views

app_name="UserLogout"
urlpatterns = [
	path('', views.logout_view, name="LogoutPage")
]
