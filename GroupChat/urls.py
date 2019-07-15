from django.urls import path

from . import views 

app_name="GuildChat"
urlpatterns = [
	path('',views.GroupChat,name="GroupChat")	

]
