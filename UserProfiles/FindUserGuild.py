#Non project imports

#Project imports
from GuildCreation.models import GuildModel, MemberListModel

#This function does as it's name implies
#Firstly, it checks all availible slots in all guilds
#Checking if the current user is in any
#If they are not, none is returned
#If they are, the Guild to which they are part of
#And a varible that specifies which slot they are in
#Is returned
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
            return CheckUserMember1.Guild

        elif CheckUserMember2 != None:
            return CheckUserMember2.Guild

        elif CheckUserMember3 != None:
            return CheckUserMember3.Guild

        elif CheckUserMember4 != None:
            return CheckUserMember4.Guild

        elif CheckUserMember5 != None:
            return CheckUserMember5.Guild
