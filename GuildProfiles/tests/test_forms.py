#Non project imports
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import os

#Project imports
from GuildProfiles.forms import UpdateGuildProfileModelForm


dirname = os.path.dirname(__file__)
# Create your tests here.
class UpdateGuildProfileFormTests(TestCase):

    def test_form_success_on_input(self):
        form = UpdateGuildProfileModelForm(data={'GuildProfileBio':'rqeuioqwiuoqrw',
                                          'GuildProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'GuildProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_bio(self):
        form = UpdateGuildProfileModelForm(data={'GuildProfileBio':'',
                                          'GuildProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'GuildProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_website(self):
        form = UpdateGuildProfileModelForm(data={'GuildProfileBio':'sdfafsdasdfafsd',
                                          'GuildProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'GuildProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_profileimage(self):
        form = UpdateGuildProfileModelForm(data={'GuildProfileBio':'sdfafsdasdfafsd',
                                          'GuildProfileImage':'',
                                          'GuildProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_headerimage(self):
        form = UpdateGuildProfileModelForm(data={'GuildProfileBio':'sdfafsdasdfafsd',
                                          'GuildProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'GuildProfileHeader':''})
        self.assertTrue(form.is_valid())
