#Non project imports
from django.db import models
import datetime
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.contrib.auth.models import User

#Project imports
from GuildCreation.models import GuildModel
from GuildProfiles.models import GuildProfileModel
from .tokens import NumberGenerator

# Create your models here.
class PostModel(models.Model):
    Id = models.AutoField(primary_key=True)
    PostGuild = models.ForeignKey(GuildModel, on_delete=models.CASCADE)
    PostGuildProfile = models.ForeignKey(GuildProfileModel, on_delete=models.CASCADE, null=True, blank=True)
    PostReply = models.ForeignKey('PostModel', on_delete=models.CASCADE, null=True, blank=True)
    PostBody = models.TextField(max_length=500)
    PostDate = models.DateField(default=datetime.date.today)
    PostLink = models.BigIntegerField(default=NumberGenerator())
    SearchVector = SearchVectorField(null=True)

    class Meta(object):
        indexes = [GinIndex(fields=['SearchVector'])]

class Like(models.Model):
    Id = models.AutoField(primary_key=True)
    PostRelation = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    UserRelation = models.ForeignKey(User, on_delete=models.CASCADE)
