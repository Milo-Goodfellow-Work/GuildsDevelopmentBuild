from django.db import models
from django.contrib.auth.models import User
from GuildCreation.models import GuildModel
from UserProfiles.models import UserProfileModel


# Create your models here.
class Message(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    ProfId = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, default=None)
    GuildId = models.ForeignKey(GuildModel, on_delete=models.CASCADE)
    MessageBody = models.CharField(max_length=300)
