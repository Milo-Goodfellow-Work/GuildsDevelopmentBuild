from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class UserPostModel(models.Model):
    Id = models.AutoField(primary_key=True)
    PostUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    PostBody = models.TextField(max_length=300)
    PostDate = models.DateField(default=datetime.date.today)
