#Non project imports
from django.urls import path

#Project imports
from . import views

app_name='GuildProfiles'
urlpatterns = [
    path('UpdateGuildProfile/', views.UpdateGuildProfileView, name="UpdateGuildProfile"),
    path('<Guildname>/', views.GuildProfileView, name="GuildProfile")

]
