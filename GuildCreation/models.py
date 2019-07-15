#Non project imports
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

#Project imports
from .tokens import NumberGenerator

# Create your models here.

class GuildModel(models.Model):
    Id = models.AutoField(primary_key=True)
    GuildName = models.CharField(max_length=30)
    GuildSize = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(2)])
    GuildInvite = models.BigIntegerField()

#This model is a bit of hack to allow for users to join guilds without a foreign key in the user model
#This is because of poor forsight on my end
#This will need a re-write
class MemberListModel(models.Model):
    Guild = models.OneToOneField(GuildModel, on_delete=models.CASCADE, null=True, blank=True)
    GuildUser1 = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE, related_name='e')
    GuildUser2 = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE, related_name='d')
    GuildUser3 = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE, related_name='c')
    GuildUser4 = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE, related_name='b')
    GuildUser5 = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE, related_name='a')
