#Non project imports
from django.urls import path

#Project imports
from . import views

app_name = 'GuildPosts'
urlpatterns = [
    path('Post/', views.PostGuildView, name="GuildPost"),
    path('PostReply/<PostLink>', views.PostGuildReplyView, name="GuildReply"),
    path('Like/<PostLink>', views.PostGuildLikeView, name="Like")

]
