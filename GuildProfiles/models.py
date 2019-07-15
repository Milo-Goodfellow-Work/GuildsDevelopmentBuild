#Non project imports
from django.db import models
import datetime

#Project imports
from GuildCreation.models import GuildModel

# Create your models here.
class GuildProfileModel(models.Model):
    Id = models.AutoField(primary_key=True)
    GuildProfileRelation = models.OneToOneField(GuildModel, on_delete=models.CASCADE)
    GuildProfileBio = models.TextField(max_length=300, blank=True, null=True)
    GuildProfileJoinDate = models.DateField(default=datetime.date.today)
    GuildProfileImage = models.ImageField(upload_to="GuildProfiles/", default="GuildProfiles/Defaults/Blank.png", blank=True, null=True)
    GuildProfileHeader = models.ImageField(upload_to="GuildProfiles/", default="GuildProfiles/Defaults/BlankWhite.png", blank=True, null=True)
