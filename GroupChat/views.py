from django.shortcuts import render
from django.http import HttpResponse

from .models import Message
from .forms import ChatModelForm

from UserProfiles.models import UserProfileModel
from .FindUserGuild import FindUserGuild

# Create your views here.
def GroupChat(request):
    MessageList = []
    UserProf = []
    if request.method == 'POST':
        MessageList = Message.objects.filter(GuildId = (FindUserGuild(request.user.id)).Id)
        form = ChatModelForm(request.POST)
        if form.is_valid():
            Chat = Message()
            Chat.UserId = request.user
            Chat.GuildId = FindUserGuild(request.user.id)
            Chat.ProfId = UserProfileModel.objects.get(UserProfileRelation = request.user)
            Chat.MessageBody = form.cleaned_data['MessageBody']
            Chat.save()

    else:
        MessageList = Message.objects.filter(GuildId = (FindUserGuild(request.user.id)).Id)
        form = ChatModelForm()

    return render(request, 'GroupChat/GroupChat.html', {'form': form, 'MessageList': MessageList, 'Username':request.user.id})
