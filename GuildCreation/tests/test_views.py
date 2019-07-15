#Non project imports
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

#Project imports
from GuildCreation import urls
from GuildCreation.models import GuildModel, MemberListModel

# Create your tests here.
class GuildCreateViewTests(TestCase):

    def test_page_redirect_no_login(self):
        checker = self.client.get(reverse('GuildLaunch:GuildCreate'))

        self.assertEqual(checker.status_code, 302)

    def test_page_functions_on_login(self):
        user = User.objects.create(username="rqeuioqwiuoqrw")
        user.set_password('uweruiy1oui79')
        user.save()
        c = self.client
        c.login(username='rqeuioqwiuoqrw', password="uweruiy1oui79")
        checker = c.get(reverse('GuildLaunch:GuildCreate'))

        self.assertEqual(checker.status_code, 200)

    def test_view_uses_correct_template(self):
        user = User.objects.create(username="rqeuioqwiuoqrw")
        user.set_password('uweruiy1oui79')
        user.save()
        c = self.client
        c.login(username='rqeuioqwiuoqrw', password="uweruiy1oui79")
        checker = c.get(reverse('GuildLaunch:GuildCreate'))

        self.assertEqual(checker.status_code, 200)
        self.assertTemplateUsed(checker, 'GuildCreation/CreateGuild.html')

class GuildJoinViewTests(TestCase):

    def test_page_redirect_no_login(self):
        checker = self.client.get(reverse('GuildLaunch:JoinGuild', kwargs={'Key':'5'}))

        self.assertEqual(checker.status_code, 302)

    def test_page_functions_on_login(self):
        user = User.objects.create(username="rqeuioqwiuoqrw")
        user.set_password('uweruiy1oui79')
        user.save()
        c = self.client
        c.login(username='rqeuioqwiuoqrw', password="uweruiy1oui79")
        checker = c.get(reverse('GuildLaunch:JoinGuild', kwargs={'Key':'5'}))

        self.assertEqual(checker.status_code, 200)
