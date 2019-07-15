#Non project imports
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


#Project imports
from GuildCreation.models import GuildModel, MemberListModel
from GuildProfiles.views import GuildProfileView
from .models import GuildFollowerModel
from Notifications.models import Notification


# Create your views here.

#This view first attempts to check if a user is following a guild
#It does this in the form of a try except statement
#If there is an exception, and there is no code error
#The only error that can occur is a failure to find that pre-existing relation
#A new try except runs that attempts to create a relation
#If it fails, assuming the same as before
#The guild doesn't exist.
#A 404 is raised
@login_required
def CreateFollowRelationView(request, GuildName):
    try:
        StoreFollowingGuild = GuildModel.objects.get(GuildName=GuildName)
        CheckerUserFollowsGuild = GuildFollowerModel.objects.get(GuildFollowed=StoreFollowingGuild, UserFollowing = request.user)
        return redirect('GuildProfiles:GuildProfile', Guildname=GuildName)

    except:
        GuildRelation = GuildFollowerModel()
        NewNotification1 = Notification()
        NewNotification2 = Notification()
        NewNotification3 = Notification()
        NewNotification4 = Notification()
        NewNotification5 = Notification()
        GuildRelation.GuildFollowed = GuildModel.objects.get(GuildName=GuildName)
        GuildRelation.UserFollowing = request.user
        TempSave = MemberListModel.objects.get(Guild=GuildModel.objects.get(GuildName = GuildName))
        NewNotification1.UserNotify = TempSave.GuildUser1
        NewNotification2.UserNotify = TempSave.GuildUser2
        NewNotification3.UserNotify = TempSave.GuildUser3
        NewNotification4.UserNotify = TempSave.GuildUser4
        NewNotification5.UserNotify = TempSave.GuildUser5

        NewNotification1.NotifyMessage = "Your guild has a new follower!"
        NewNotification2.NotifyMessage = "Your guild has a new follower!"
        NewNotification3.NotifyMessage = "Your guild has a new follower!"
        NewNotification4.NotifyMessage = "Your guild has a new follower!"
        NewNotification5.NotifyMessage = "Your guild has a new follower!"

        NewNotification1.save()
        NewNotification2.save()
        NewNotification3.save()
        NewNotification4.save()
        NewNotification5.save()
        GuildRelation.save()

    return redirect('GuildProfiles:GuildProfile', Guildname=GuildName)
