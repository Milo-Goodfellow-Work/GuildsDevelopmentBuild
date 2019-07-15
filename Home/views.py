from django.shortcuts import render
from django.contrib.auth.models import User
from GuildPosts.models import PostModel, Like
from UserPosts.models import UserPostModel
from Follow.models import GuildFollowerModel
from UserProfiles.models import UserProfileModel
from GuildCreation.models import MemberListModel
from .FindUserGuild import FindUserGuild
from GuildProfiles.models import GuildProfileModel
from GroupChat.models import Message
from GroupChat.forms import ChatModelForm
from Notifications.models import Notification

# Create your views here.
def HomeView(request):
    UserName = request.user.username
    UserProfile = UserProfileModel.objects.get(UserProfileRelation = request.user)
    GuildName = (FindUserGuild(request.user)).Guild.GuildName
    GuildProfile = GuildProfileModel.objects.get(GuildProfileRelation = FindUserGuild(request.user).Guild)
    FollowedList = GuildFollowerModel.objects.filter(UserFollowing = request.user)
    NotificationLi = Notification.objects.filter(UserNotify = request.user)
    ProfileList = []
    FollowerPostList = []
    Details = []
    Temp=[]
    Temp2=[]
    MessageList = []
    UserProf = []
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

    for i in FollowedList:
        FollowerPostList.append(PostModel.objects.filter(PostGuild = i.GuildFollowed))

    for i in FollowerPostList:
        for k in i:
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
            Details.append(Temp)
            Temp = []
        Temp2=[]
        Temp=[]




    UserPosts = UserPostModel.objects.filter(PostUser = User.objects.get(username=request.user.username))
    return render(request, 'Home/Home.html', {'NotificationLi':NotificationLi,'form':form ,'MessageList': MessageList, 'GuildName': GuildName,'GuildProfile':GuildProfile,'UserProfile':UserProfile,'FollowerPostList':FollowerPostList, 'UserPosts':UserPosts, 'UserName':UserName, 'ProfileList':ProfileList, 'Details':Details})
