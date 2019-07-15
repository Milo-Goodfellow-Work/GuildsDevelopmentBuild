#Non project imports
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
import os

#Project imports
from GuildProfiles import urls

# Create your tests here.

dirname = os.path.dirname(__file__)
class UserProfileUpdateViewTests(TestCase):

    def set_up(self):
        user = User.objects.create(username='rqeuioqwiuoqrw')
        user.set_password('uweruiy1oui79')

        user.save()


    def test_redirect_page_exists_at_view_url(self):
        checker = self.client.get('/GuildProfiles/UpdateGuildProfile')

        self.assertEqual(checker.status_code, 301)

    def test_page_exists_at_view_name(self):
        checker = self.client.get(reverse('GuildProfiles:UpdateGuildProfile'))

        self.assertEqual(checker.status_code, 302)

    def test_page_exists_at_view_url(self):
        c = self.client
        c.login(username='rqeuioqwiuoqrw', password="uweruiy1oui79")
        checker = c.get('/GuildProfiles/UpdateGuildProfile')

        self.assertTrue(checker.status_code, 200)


class UserProfileViewTests(TestCase):

    def set_up(self):
        user = User.objects.create(username='rqeuioqwiuoqrw')
        user.set_password('uweruiy1oui79')

        user.save()


    def test_redirect_page_exists_at_view_url(self):
        checker = self.client.get('/GuildProfiles/UpdateGuildProfile')

        self.assertEqual(checker.status_code, 301)

    def test_page_exists_at_view_url(self):
        c = self.client
        c.login(username='rqeuioqwiuoqrw', password="uweruiy1oui79")
        checker = c.get('/UserProfiles/rqeuioqwiuoqrw')

        self.assertTrue(checker.status_code, 200)
