#Non project imports
from django.shortcuts import render, redirect, reverse
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404


#Project imports
from .models import PostModel, Like
from Notifications.models import Notification
from GuildCreation.models import MemberListModel, GuildModel
from GuildProfiles.models import GuildProfileModel
from .forms import GuildPostModelForm
from .FindUserGuild import FindUserGuild
from .tokens import NumberGenerator

# Create your views here.

def PostGuildView(request):
    UserGuild = FindUserGuild(request.user)
    if UserGuild != None:
        if request.method == 'POST':
            form = GuildPostModelForm(request.POST)
            Post = PostModel()
            if form.is_valid():
                Post.PostBody = form.cleaned_data['PostBody']
                Post.PostGuild = UserGuild.Guild
                Post.PostGuildProfile = GuildProfileModel.objects.get(GuildProfileRelation=UserGuild.Guild)
                Post.PostLink = NumberGenerator()
                Post.save()
                return redirect('Home:Feed')

        else:
            form = GuildPostModelForm()
        return render(request, 'GuildPosts/GuildPost.html', {'form': form})
    else:
        form = GuildPostModelForm()
        raise Http404

def PostGuildReplyView(request, PostLink):
    UserGuild = FindUserGuild(request.user)
    if UserGuild != None:
        if request.method == 'POST':
            form = GuildPostModelForm(request.POST)
            Post = PostModel()
            if form.is_valid():
                Post.PostBody = form.cleaned_data['PostBody']
                Post.PostGuild = UserGuild.Guild
                Post.PostReply = PostModel.objects.get(PostLink=PostLink)
                Post.PostGuildProfile = GuildProfileModel.objects.get(GuildProfileRelation=UserGuild.Guild)
                Post.PostLink = NumberGenerator()

                NewNotification1 = Notification()
                NewNotification2 = Notification()
                NewNotification3 = Notification()
                NewNotification4 = Notification()
                NewNotification5 = Notification()

                TempSave = MemberListModel.objects.get(Guild=GuildModel.objects.get(GuildName = Post.PostReply.PostGuild.GuildName))

                NewNotification1.UserNotify = TempSave.GuildUser1
                NewNotification2.UserNotify = TempSave.GuildUser2
                NewNotification3.UserNotify = TempSave.GuildUser3
                NewNotification4.UserNotify = TempSave.GuildUser4
                NewNotification5.UserNotify = TempSave.GuildUser5

                NewNotification1.NotifyMessage = "Your guilds post has a new reply!"
                NewNotification2.NotifyMessage = "Your guilds post has a new reply!"
                NewNotification3.NotifyMessage = "Your guilds post has a new reply!"
                NewNotification4.NotifyMessage = "Your guilds post has a new reply!"
                NewNotification5.NotifyMessage = "Your guilds post has a new reply!"

                NewNotification1.save()
                NewNotification2.save()
                NewNotification3.save()
                NewNotification4.save()
                NewNotification5.save()

                Post.save()

        else:
            form = GuildPostModelForm()
        return render(request, 'GuildPosts/GuildPost.html', {'form': form})
    else:
        raise Http404

def PostGuildLikeView(request, PostLink):
    LikeVar = Like()
    Exist = 0
    LikeVar.PostRelation = get_object_or_404(PostModel, PostLink=PostLink)
    LikeVar.UserRelation = request.user

    try:
        Exist = Like.objects.get(PostRelation = LikeVar.PostRelation, UserRelation = request.user)
        Exist.delete()
        Exist.save()

    except:
        NewNotification1 = Notification()
        NewNotification2 = Notification()
        NewNotification3 = Notification()
        NewNotification4 = Notification()
        NewNotification5 = Notification()

        TempSave = MemberListModel.objects.get(Guild=GuildModel.objects.get(GuildName = LikeVar.PostRelation.PostGuild.GuildName))
        NewNotification1.UserNotify = TempSave.GuildUser1
        NewNotification2.UserNotify = TempSave.GuildUser2
        NewNotification3.UserNotify = TempSave.GuildUser3
        NewNotification4.UserNotify = TempSave.GuildUser4
        NewNotification5.UserNotify = TempSave.GuildUser5

        NewNotification1.NotifyMessage = "Your guilds post has a new like!"
        NewNotification2.NotifyMessage = "Your guilds post has a new like!"
        NewNotification3.NotifyMessage = "Your guilds post has a new like!"
        NewNotification4.NotifyMessage = "Your guilds post has a new like!"
        NewNotification5.NotifyMessage = "Your guilds post has a new like!"

        NewNotification1.save()
        NewNotification2.save()
        NewNotification3.save()
        NewNotification4.save()
        NewNotification5.save()

        LikeVar.save()

    return redirect('Home:Feed')
