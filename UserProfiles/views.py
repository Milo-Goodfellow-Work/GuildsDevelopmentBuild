#Non project imports
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404

#Project imports
from Guilds.settings import MEDIA_URL
from .forms import UpdateUserProfileForm
from .models import UserProfileModel
from UserPosts.models import UserPostModel
from GroupChat.models import Message
from GroupChat.forms import ChatModelForm
from Notifications.models import Notification
from GuildProfiles.models import GuildProfileModel
from .FindUserGuild import FindUserGuild


# Create your views here.


#This view tries to update a users profile
#If they lack a profile, it creates a new one in the database
@login_required
def UpdateUserProfileView(request):
    if request.method == "POST":
        form = UpdateUserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            ProfileVar = UserProfileModel()
            try:
                UpdateUserProfile = UserProfileModel.objects.get(UserProfileRelation = request.user)
                UpdateUserProfile.UserProfileBio = form.cleaned_data['UserProfileBio']
                UpdateUserProfile.UserProfileWebsite = form.cleaned_data['UserProfileWebsite']
                UpdateUserProfile.UserProfileImage = form.cleaned_data['UserProfileImage']
                UpdateUserProfile.UserProfileHeader = form.cleaned_data['UserProfileHeader']
                print(form.cleaned_data['UserProfileHeader'])
                UpdateUserProfile.save()
                return redirect('Home:Feed')

            except:
                ProfileVar.UserProfileBio = form.cleaned_data['UserProfileBio']
                ProfileVar.UserProfileWebsite = form.cleaned_data['UserProfileWebsite']
                ProfileVar.UserProfileImage = form.cleaned_data['UserProfileImage']
                ProfileVar.UserProfileRelation = request.user
                ProfileVar.UserProfileHeader = form.cleaned_data['UserProfileHeader']
                ProfileVar.save()
                return redirect('Home:Feed')

    else:
        form = UpdateUserProfileForm()

    return render(request, 'UserProfiles/UpdateProfile.html', {'form' : form})

#This view gets the relevant information for a user profile
#Adds it to a list
#And passes it to the render
@login_required
def UserProfileView(request, Username):
    UserName = request.user.username
    NotificationLi = Notification.objects.filter(UserNotify = request.user)
    ProfileList = []
    FollowerPostList = []
    Details = []
    Temp=[]
    Temp2=[]
    MessageList = []
    UserProf = []
    MessageList = Message.objects.filter(GuildId = FindUserGuild(request.user.id))

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

    try:
        UsernameUser = User.objects.get(username=Username)
        ProfileUserId = UsernameUser.id
        ProfileUsername = UsernameUser.username
        UsernameUserProfile = UserProfileModel.objects.get(UserProfileRelation=ProfileUserId)
        ProfileBio = UsernameUserProfile.UserProfileBio
        ProfileImage = UsernameUserProfile.UserProfileImage.url
        ProfileHeader = UsernameUserProfile.UserProfileHeader.url
        ProfileLink = UsernameUserProfile.UserProfileWebsite
        UserPosts = UserPostModel.objects.filter(PostUser = User.objects.get(username=Username))
        Guild = FindUserGuild(ProfileUserId)
        GuildProf = GuildProfileModel.objects.get(GuildProfileRelation=Guild)
        ProfileInformation = [ProfileUsername, ProfileBio, ProfileLink, ProfileImage, ProfileHeader, Guild, GuildProf]

    except:
        raise Http404;

    return render(request, 'UserProfiles/UserProfile.html', {'form':form, 'NotificationLi':NotificationLi, 'MessageList':MessageList , 'ProfileInformation': ProfileInformation, 'UserPosts':UserPosts, 'UserName': UserName})
