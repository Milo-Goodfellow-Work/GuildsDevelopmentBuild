#Non project imports
from django.db import models
from django.conf import settings

#Project imports 
from GuildCreation.models import GuildModel

# Create your models here.
class GuildFollowerModel(models.Model):
    Id = models.AutoField(primary_key=True)
    UserFollowing = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    GuildFollowed = models.ForeignKey(GuildModel, on_delete=models.CASCADE)
