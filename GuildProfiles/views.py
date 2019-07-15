#Non project imports
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404

#Project imports
from Guilds.settings import MEDIA_URL
from .forms import UpdateGuildProfileModelForm
from .models import GuildProfileModel
from GuildCreation.models import GuildModel, MemberListModel
from .FindUserGuild import FindUserGuild
from GuildPosts.models import PostModel

# Create your views here.


#This view tries to update a users profile
#If they lack a profile, it creates a new one in the database
@login_required
def UpdateGuildProfileView(request):
    UserGuild = FindUserGuild(request.user)
    if UserGuild != None:
        if request.method == "POST":
            form = UpdateGuildProfileModelForm(request.POST, request.FILES)
            if form.is_valid():
                ProfileVar = GuildProfileModel()
                try:
                    UpdateGuildProfile = GuildProfileModel.objects.get(GuildProfileRelation = UserGuild.Guild)
                    UpdateGuildProfile.GuildProfileBio = form.cleaned_data['GuildProfileBio']
                    UpdateGuildProfile.GuildProfileImage = form.cleaned_data['GuildProfileImage']
                    UpdateGuildProfile.GuildProfileHeader = form.cleaned_data['GuildProfileHeader']
                    UpdateGuildProfile.save()
                    return redirect('Home:Feed')

                except:
                    ProfileVar.GuildProfileBio = form.cleaned_data['GuildProfileBio']
                    ProfileVar.GuildProfileImage = form.cleaned_data['GuildProfileImage']
                    ProfileVar.GuildProfileRelation = UserGuild.Guild
                    ProfileVar.GuildProfileHeader = form.cleaned_data['GuildProfileHeader']
                    ProfileVar.save()
                    return redirect('Home:Feed')

        else:
            form = UpdateGuildProfileModelForm()

        return render(request, 'GuildProfiles/UpdateGuildProfile.html', {'form' : form})

    raise Http404

#This view gets the relevant information for a Guild profile
#Adds it to a list
#And passes it to the render
@login_required
def GuildProfileView(request, Guildname):
    UserName = request.user.username
    try:
        GuildnameGuild = GuildModel.objects.get(GuildName=Guildname)
        ProfileGuildId = GuildnameGuild.Id
        ProfileGuildname = GuildnameGuild.GuildName
        GuildnameGuildProfile = GuildProfileModel.objects.get(GuildProfileRelation=ProfileGuildId)
        ProfileBio = GuildnameGuildProfile.GuildProfileBio
        ProfileImage = GuildnameGuildProfile.GuildProfileImage.url
        ProfileHeader = GuildnameGuildProfile.GuildProfileHeader.url
        GuildMemberModel = MemberListModel.objects.get(Guild=GuildnameGuild)
        MemberModelMember1 = GuildMemberModel.GuildUser1
        MemberModelMember2 = GuildMemberModel.GuildUser2
        MemberModelMember3 = GuildMemberModel.GuildUser3
        MemberModelMember4 = GuildMemberModel.GuildUser4
        MemberModelMember5 = GuildMemberModel.GuildUser5
        UserPosts = PostModel.objects.filter(PostGuild = GuildModel.objects.get(GuildName=Guildname))
        ProfileInformation = [ProfileGuildname, ProfileBio, ProfileImage, ProfileHeader, MemberModelMember1, MemberModelMember2, MemberModelMember3, MemberModelMember4, MemberModelMember5]
    except:
        raise Http404

    return render(request, 'GuildProfiles/GuildProfile.html', {'ProfileInformation': ProfileInformation, 'UserPosts':UserPosts, 'UserName':UserName})
