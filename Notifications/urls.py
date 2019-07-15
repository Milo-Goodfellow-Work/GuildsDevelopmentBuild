from django.urls import path

from . import views

app_name = "NotificationsApp"
urlpatterns = [
    path('', views.Notifications, name="Notifications")

]
