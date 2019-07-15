#Non project imports
from django.urls import path

#Project imports
from . import views

app_name = 'UserProfiles'
urlpatterns = [
    path('UpdateProfile/', views.UpdateUserProfileView , name="UpdateProfile"),
    path('Profiles/<Username>/', views.UserProfileView, name="UserProfile")

]
