#Non project imports
from django.test import TestCase
from django.urls import reverse

#Project imports
from GuildCreation.forms import CreateGuildForm

# Create your tests here.
class CreateGuildFormTests(TestCase):

    def test_create_guild_form_success(self):
        form = CreateGuildForm(data={'GuildName': 'AnEpicGuild!',
                                    'GuildSize': '2'})

        self.assertTrue(form.is_valid())

    def test_create_guild_form_fail_on_name(self):
        form = CreateGuildForm(data={'GuildName': '',
                                    'GuildSize': '2'})

        self.assertFalse(form.is_valid())

    def test_create_guild_form_fail_on_size(self):
        form = CreateGuildForm(data={'GuildName': 'AnEpicGuild!',
                                    'GuildSize': '10000000'})

        self.assertFalse(form.is_valid())
