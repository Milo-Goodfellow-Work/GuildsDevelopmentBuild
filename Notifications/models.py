from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    UserNotify = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    NotifyMessage = models.CharField(max_length=100)
