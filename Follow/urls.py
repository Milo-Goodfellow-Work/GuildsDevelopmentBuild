#Non project imports
from django.urls import path

#Project imports
from . import views

app_name = "Follow"
urlpatterns = [
    path('<GuildName>/', views.CreateFollowRelationView, name="FollowGuild"),

]
