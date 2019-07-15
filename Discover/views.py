#Non project imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Project imports
from GuildPosts.models import PostModel
from UserProfiles.models import UserProfileModel
from GroupChat.models import Message
from GroupChat.forms import ChatModelForm
from Notifications.models import Notification
from GuildProfiles.models import GuildProfileModel
from .FindUserGuild import FindUserGuild
from GuildPosts.models import Like

# Create your views here.

def Discover(request):
    PostList = PostModel.objects.filter()
    UserName = request.user.username
    NotificationLi = Notification.objects.filter(UserNotify = request.user)
    MessageList = Message.objects.filter(GuildId = FindUserGuild(request.user.id))
    Temp = []
    Temp2 = []
    FullList = []

    if request.method == 'POST':
        form = ChatModelForm(request.POST)
        if form.is_valid():
            Chat = Message()
            Chat.UserId = request.user
            Chat.GuildId = FindUserGuild(request.user.id)
            Chat.MessageBody = form.cleaned_data['MessageBody']
            Chat.ProfId = UserProfileModel.objects.get(UserProfileRelation = request.user)
            Chat.save()
    else:
        form = ChatModelForm()

    for k in PostList:
        try:
            Temp.append(k.PostGuildProfile.GuildProfileImage)
        except:
            Temp.append("")
        Temp.append(k.PostGuild.GuildName)
        Temp.append(k.PostDate)
        Temp.append(k.PostBody)
        Temp.append(k.PostLink)
        Temp.append(len(Like.objects.filter(PostRelation=k)))
        try:
            Temp2.append(UserProfileModel.objects.get(UserProfileRelation=((MemberListModel.objects.get(Guild=k.PostGuild)).GuildUser1)))
        except:
            pass
        try:
            Temp2.append(UserProfileModel.objects.get(UserProfileRelation=((MemberListModel.objects.get(Guild=k.PostGuild)).GuildUser2)))
        except:
            pass
        try:
            Temp2.append(UserProfileModel.objects.get(UserProfileRelation=((MemberListModel.objects.get(Guild=k.PostGuild)).GuildUser3)))
        except:
            pass
        try:
            Temp2.append(UserProfileModel.objects.get(UserProfileRelation=((MemberListModel.objects.get(Guild=k.PostGuild)).GuildUser4)))
        except:
            pass
        try:
            Temp2.append(UserProfileModel.objects.get(UserProfileRelation=((MemberListModel.objects.get(Guild=k.PostGuild)).GuildUser5)))
        except:
            pass
        Temp.append(Temp2)
        FullList.append(Temp)
        Temp = []
        Temp2 = []

    return render(request, 'Discover/Discover.html', {'FullList':FullList,'form':form, 'NotificationLi':NotificationLi, 'MessageList':MessageList,'PostList':PostList, 'UserName':request.user.username})
