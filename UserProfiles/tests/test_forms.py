#Non project imports
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import os

#Project imports
from UserProfiles.forms import UpdateUserProfileForm


dirname = os.path.dirname(__file__)
# Create your tests here.
class UpdateUserProfileFormTests(TestCase):

    def test_form_success_on_input(self):
        form = UpdateUserProfileForm(data={'UserProfileBio':'rqeuioqwiuoqrw',
                                          'UserProfileWebsite':'fgjkfgdjnklfgsdu',
                                          'UserProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'UserProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_bio(self):
        form = UpdateUserProfileForm(data={'UserProfileBio':'',
                                          'UserProfileWebsite':'fgjkfgdjnklfgsdu',
                                          'UserProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'UserProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_website(self):
        form = UpdateUserProfileForm(data={'UserProfileBio':'sdfafsdasdfafsd',
                                          'UserProfileWebsite':'',
                                          'UserProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'UserProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_profileimage(self):
        form = UpdateUserProfileForm(data={'UserProfileBio':'sdfafsdasdfafsd',
                                          'UserProfileWebsite':'asdasdfasdfasdf',
                                          'UserProfileImage':'',
                                          'UserProfileHeader':open(os.path.join(dirname, "TestImages/TestImage.jpg"))})
        self.assertTrue(form.is_valid())

    def test_form_success_on_blank_headerimage(self):
        form = UpdateUserProfileForm(data={'UserProfileBio':'sdfafsdasdfafsd',
                                          'UserProfileWebsite':'',
                                          'UserProfileImage':open(os.path.join(dirname, "TestImages/TestImage.jpg")),
                                          'UserProfileHeader':''})
        self.assertTrue(form.is_valid())
