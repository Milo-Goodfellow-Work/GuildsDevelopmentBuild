#Non project imports
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse

#Project imports
from GuildPosts.models import PostModel
from .FindUserGuild import FindUserGuild
from .forms import SearchForm
from GuildPosts.models import PostModel, Like
from Notifications.models import Notification
from GroupChat.models import Message

# Create your views here.
def SearchView(request):
    NotificationLi = Notification.objects.filter(UserNotify = request.user)
    MessageList = Message.objects.filter(GuildId = (FindUserGuild(request.user.id)).Guild)

    PostList = None
    Temp = []
    Temp2 = []
    FullList = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            PostList = PostModel.objects.annotate(search=SearchVector('PostBody')).filter(search=form.cleaned_data['Search'])

            for k in PostList:
                Temp = []
                Temp2 = []

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



    else:
        form = SearchForm()

    del Temp
    del Temp2

    return render(request, 'FullSearch/Search.html', {'MessageList':MessageList, 'NotificationLi': NotificationLi, 'FullList':FullList,'form':form, 'PostList':PostList, 'UserName': request.user.username})
