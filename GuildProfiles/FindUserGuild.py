#Non project imports

#Project imports
from GuildCreation.models import GuildModel, MemberListModel


def FindUserGuild(UserToFind):

        try:
            CheckUserMember1 = MemberListModel.objects.get(GuildUser1=UserToFind)

        except:
            CheckUserMember1 = None

        try:
            CheckUserMember2 = MemberListModel.objects.filter(GuildUser2=UserToFind)
        except:
            CheckUserMember2 = None

        try:
            CheckUserMember3 = MemberListModel.objects.filter(GuildUser3=UserToFind)

        except:
            CheckUserMember3 = None

        try:
            CheckUserMember4 = MemberListModel.objects.filter(GuildUser4=UserToFind)
        except:
            CheckUserMember4 = None

        try:
            CheckUserMember5 = MemberListModel.objects.filter(GuildUser5=UserToFind)
        except:
            CheckUserMember5 = None



        if not CheckUserMember1 and not CheckUserMember2 and not CheckUserMember3 and not CheckUserMember4 and not CheckUserMember5:
            return None

        elif CheckUserMember1 != None:
            return CheckUserMember1

        elif CheckUserMember2 != None:
            return CheckUserMember2

        elif CheckUserMember3 != None:
            return CheckUserMember3

        elif CheckUserMember4 != None:
            return CheckUserMember4

        elif CheckUserMember5 != None:
            return CheckUserMember5
