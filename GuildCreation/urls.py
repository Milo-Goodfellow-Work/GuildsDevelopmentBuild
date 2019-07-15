#Non project imports
from django.urls import path

#Project imports
from . import views

app_name="GuildLaunch"
urlpatterns=[
    path('CreateGuild/', views.GuildCreateView, name="GuildCreate"),
    path('Join/<Key>/', views.GuildJoinView, name="JoinGuild"),
    path('LeaveGuild/', views.LeaveGuild, name="LeaveGuild")

]
