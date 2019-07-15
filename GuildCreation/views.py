#Non project imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

#Project imports
from .forms import CreateGuildForm
from .models import GuildModel, MemberListModel
from .tokens import NumberGenerator
from . import urls

# Create your views here.

#This view either sets the form to CreateGuildForm
#Or if the user is submiting a form, validates the form
#Then sets the user to be part of this Guild after removing them from their current guild if they are in one
@login_required
def GuildCreateView(request):
    if request.method == 'POST':
        form = CreateGuildForm(request.POST)
        if form.is_valid():
            GuildVar = GuildModel()
            GuildMemberVar = MemberListModel()
            GuildVar.GuildName = form.cleaned_data['GuildName']
            GuildVar.GuildSize = form.cleaned_data['GuildSize']
            GuildVar.GuildInvite = NumberGenerator()
            GuildVar.save()
            GuildStore = GuildModel.objects.get(GuildName=form.cleaned_data['GuildName'])

            try:
                CheckUserMember1 = MemberListModel.objects.get(GuildUser1=request.user)

            except:
                CheckUserMember1 = None

            try:
                CheckUserMember2 = MemberListModel.objects.filter(GuildUser2=request.user)
            except:
                CheckUserMember2 = None

            try:
                CheckUserMember3 = MemberListModel.objects.filter(GuildUser3=request.user)

            except:
                CheckUserMember3 = None

            try:
                CheckUserMember4 = MemberListModel.objects.filter(GuildUser4=request.user)
            except:
                CheckUserMember4 = None

            try:
                CheckUserMember5 = MemberListModel.objects.filter(GuildUser5=request.user)
            except:
                CheckUserMember5 = None

            if not CheckUserMember1 and not CheckUserMember2 and not CheckUserMember3 and not CheckUserMember4 and not CheckUserMember5:
                GuildMemberVar.Guild = GuildStore
                GuildMemberVar.GuildUser1 = request.user
                GuildMemberVar.save()

            elif CheckUserMember1 != None:
                CheckUserMember1.GuildUser1 = None
                GuildMemberVar.Guild = GuildStore
                GuildMemberVar.GuildUser1 = request.user
                CheckUserMember1.save()
                GuildMemberVar.save()

            elif CheckUserMember2 != None:
                CheckUserMember2.GuildUser2 = None
                GuildMemberVar.Guild = GuildStore
                GuildMemberVar.GuildUser1 = request.user
                CheckUserMember2.save()
                GuildMemberVar.save()

            elif CheckUserMember3 != None:
                CheckUserMember3.GuildUser3 = None
                GuildMemberVar.Guild = GuildStore
                GuildMemberVar.GuildUser1 = request.user
                CheckUserMember3.save()
                GuildMemberVar.save()

            elif CheckUserMember4 != None:
                CheckUserMember4.GuildUser4 = None
                GuildMemberVar.Guild = GuildStore
                GuildMemberVar.GuildUser1 = request.user
                CheckUserMember4.save()
                GuildMemberVar.save()

            elif CheckUserMember5 != None:
                CheckUserMember5.GuildUser5 = None
                GuildMemberVar.Guild = GuildStore
                GuildMemberVar.GuildUser1 = request.user
                CheckUserMember5.save()
                GuildMemberVar.save()

            return redirect('GuildLaunch:GuildCreate')

    else:
        form = CreateGuildForm()

    return render(request, 'GuildCreation/CreateGuild.html', {'form': form})

#This view presents a user with the ability to join a guild
#Should they first leave the one they are currently in
#If they Guild they are trying to join doesn't exist or is full
#They are not joined
@login_required
def GuildJoinView(request, Key):

    try:
        GuildStore = GuildModel.objects.get(GuildInvite=Key)
        JoinMemberVar = MemberListModel.objects.get(Guild=GuildStore)
        JoinGuildName = GuildStore.GuildName
        CurrentUser = request.user

        #This code is a huge bloat
        #It absolutely MUST be patched out
        #As it wastes a ton of time
        #It exists only as long as models.py has the MemberListModel
        #A model that can be removed by adding a foreign key to the User model (This is very dificult at this stage)
        if request.method=="POST":

            try:
                CheckUserMember1 = MemberListModel.objects.get(GuildUser1=request.user)

            except:
                CheckUserMember1 = None

            try:
                CheckUserMember2 = MemberListModel.objects.filter(GuildUser2=request.user)

            except:
                CheckUserMember2 = None

            try:
                CheckUserMember3 = MemberListModel.objects.filter(GuildUser3=request.user)

            except:
                CheckUserMember3 = None

            try:
                CheckUserMember4 = MemberListModel.objects.filter(GuildUser4=request.user)

            except:
                CheckUserMember4 = None

            try:
                CheckUserMember5 = MemberListModel.objects.filter(GuildUser5=request.user)

            except:
                CheckUserMember5 = None



            if JoinMemberVar.GuildUser1 == None or JoinMemberVar.GuildUser1 == request.user and JoinMemberVar.GuildUser2 != request.user and JoinMemberVar.GuildUser3 != request.user and JoinMemberVar.GuildUser4 != request.user and JoinMemberVar.GuildUser5 != request.user:
                JoinMemberVar.GuildUser1 = CurrentUser

            elif JoinMemberVar.GuildUser2 == None or JoinMemberVar.GuildUser2 == request.user and JoinMemberVar.GuildUser3 != request.user and JoinMemberVar.GuildUser4 != request.user and JoinMemberVar.GuildUser5 != request.user:
                JoinMemberVar.GuildUser2 = CurrentUser

            elif JoinMemberVar.GuildUser3 == None or JoinMemberVar.GuildUser3 == request.user and GuildStore.GuildSize >= 3 and JoinMemberVar.GuildUser4 != request.user and JoinMemberVar.GuildUser5 != request.user:
                JoinMemberVar.GuildUser3 = CurrentUser

            elif JoinMemberVar.GuildUser4 == None or JoinMemberVar.GuildUser4 == request.user and GuildStore.GuildSize >= 4 and JoinMemberVar.GuildUser5 != request.user:
                JoinMemberVar.GuildUser4 = CurrentUser

            elif JoinMemberVar.GuildUser5 == None or JoinMemberVar.GuildUser5 == request.user and GuildStore.GuildSize == 5:
                JoinMemberVar.GuildUser5 = CurrentUser



            if CheckUserMember1 != None:
                CheckUserMember1.GuildUser1 = None
                CheckUserMember1.save()

            elif CheckUserMember2 != None:
                CheckUserMember2.GuildUser2 = None
                CheckUserMember2.save()

            elif CheckUserMember3 != None:
                CheckUserMember3.GuildUser3 = None
                CheckUserMember3.save()

            elif CheckUserMember4 != None:
                CheckUserMember4.GuildUser4 = None
                CheckUserMember4.save()

            elif CheckUserMember5 != None:
                CheckUserMember5.GuildUser5 = None
                CheckUserMember5.save()

            return redirect('Home:Feed')

    except:
        return render(request, 'GuildCreation/GuildJoinError.html')

    return render(request, 'GuildCreation/GuildJoinChoice.html', {'JoinGuildName':JoinGuildName})


def LeaveGuild(request):
    try:
        try:
            CheckUserMember1 = MemberListModel.objects.get(GuildUser1=request.user)

        except:
            CheckUserMember1 = None

        try:
            CheckUserMember2 = MemberListModel.objects.filter(GuildUser2=request.user)

        except:
            CheckUserMember2 = None

        try:
            CheckUserMember3 = MemberListModel.objects.filter(GuildUser3=request.user)

        except:
            CheckUserMember3 = None

        try:
            CheckUserMember4 = MemberListModel.objects.filter(GuildUser4=request.user)

        except:
            CheckUserMember4 = None

        try:
            CheckUserMember5 = MemberListModel.objects.filter(GuildUser5=request.user)

        except:
            CheckUserMember5 = None

        if CheckUserMember1 != None:
            CheckUserMember1.GuildUser1 = None
            CheckUserMember1.save()

        elif CheckUserMember2 != None:
            CheckUserMember2.GuildUser2 = None
            CheckUserMember2.save()

        elif CheckUserMember3 != None:
            CheckUserMember3.GuildUser3 = None
            CheckUserMember3.save()

        elif CheckUserMember4 != None:
            CheckUserMember4.GuildUser4 = None
            CheckUserMember4.save()

        elif CheckUserMember5 != None:
            CheckUserMember5.GuildUser5 = None
            CheckUserMember5.save()


    except:
        raise Http404
