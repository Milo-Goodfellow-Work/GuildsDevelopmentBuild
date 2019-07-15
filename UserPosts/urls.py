from django.urls import path

from . import views

app_name = 'UserPosts'
urlpatterns = [
    path('Post/', views.UserPostView, name="PostUser")

]
