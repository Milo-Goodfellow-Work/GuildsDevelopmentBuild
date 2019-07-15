#Non project imports
from django.db import models
from django.conf import settings
import datetime

#Project imports

# Create your models here.
class UserProfileModel(models.Model):
    Id = models.AutoField(primary_key=True)
    UserProfileRelation = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    UserProfileBio = models.TextField(max_length=300, blank=True, null=True)
    UserProfileWebsite = models.CharField(max_length=50, blank=True, null=True)
    UserProfileJoinDate = models.DateField(default=datetime.date.today)
    UserProfileImage = models.ImageField(upload_to="UserProfiles/", default="UserProfiles/Defaults/Blank.png", blank=True, null=True)
    UserProfileHeader = models.ImageField(upload_to="UserProfiles/", default="UserProfiles/Defaults/BlankWhite.png", blank=True, null=True)
