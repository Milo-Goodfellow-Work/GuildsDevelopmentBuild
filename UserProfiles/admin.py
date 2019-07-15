#Non project imports
from django.contrib import admin

#Project imports
from .models import UserProfileModel

# Register your models here.
admin.site.register(UserProfileModel)
