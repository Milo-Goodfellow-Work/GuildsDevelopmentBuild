#Non project imports
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

#Project imports
from Follow import urls
from Follow.views import CreateFollowRelationView
from GuildCreation.models import GuildModel

#Create your tests here.
