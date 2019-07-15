from django.shortcuts import render

from UserProfiles.models import UserProfileModel
from Guilds.settings import MEDIA_URL
from UserPosts.models import UserPostModel
from GroupChat.models import Message
from GroupChat.forms import ChatModelForm
from Notifications.models import Notification
from GuildProfiles.models import GuildProfileModel
from .FindUserGuild import FindUserGuild
from GuildProfiles.models import GuildProfileModel

# Create your views here.
def GroupView(request):
    UserName = request.user.username
    UserProfile = UserProfileModel.objects.get(UserProfileRelation = request.user)
    GuildName = (FindUserGuild(request.user)).Guild.GuildName
    GuildProfile = GuildProfileModel.objects.get(GuildProfileRelation = FindUserGuild(request.user).Guild)
    NotificationLi = Notification.objects.filter(UserNotify = request.user)
    MessageList = Message.objects.filter(GuildId = (FindUserGuild(request.user.id)).Guild)

    if request.method == 'POST':
        form = ChatModelForm(request.POST)
        if form.is_valid():
            Chat = Message()
            Chat.UserId = request.user
            Chat.GuildId = FindUserGuild(request.user.id).Guild
            Chat.MessageBody = form.cleaned_data['MessageBody']
            Chat.ProfId = UserProfileModel.objects.get(UserProfileRelation = request.user)
            Chat.save()
    else:
        form = ChatModelForm()

    return render(request, 'GroupPage/GroupPage.html', {'form':form, 'NotificationLi':NotificationLi, 'MessageList':MessageList, 'UserName':UserName})
