from django.shortcuts import render

from .FindUserGuild import FindUserGuild

# Create your views here.
def SettingsLinkListView(request):
    UserName = None
    UserGuild = None
    UserGuildModel = None
    UserGuildName = None
    UserGuildModelInvite = None

    try:
        UserName = request.user.username
        UserGuild = FindUserGuild(request.user)
        UserGuildModel = UserGuild.Guild
        UserGuildName = UserGuildModel.GuildName
        UserGuildModelInvite = UserGuildModel.GuildInvite

    except:
        UserName = request.user.username

    return render(request, 'UserSettings/Settings.html', {'UserName': UserName, 'UserGuild': UserGuild, 'UserGuildName':UserGuildName, 'UserGuildModelInvite': UserGuildModelInvite, 'UserName': request.user.username})
