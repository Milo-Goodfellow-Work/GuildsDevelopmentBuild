#Non project imports
from django.contrib import admin

#Project imports
from . import models

# Register your models here.
admin.site.register(models.GuildModel)
admin.site.register(models.MemberListModel)
