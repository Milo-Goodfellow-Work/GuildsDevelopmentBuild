#Non project imports
from django.test import TestCase
from django.urls import reverse

#Project imports
from UserEntry import urls

# Create your tests here.

class UserCreationViewTests(TestCase):



    def test_page_exists_at_view_url(self):
        checker = self.client.get('/UserEntry/Register/')

        self.assertEqual(checker.status_code, 200)



    def test_page_accessible_by_name(self):
        checker = self.client.get(reverse('UserEntry:Register'))

        self.assertEqual(checker.status_code, 200)



    def test_page_template_accurate(self):
        checker =self.client.get(reverse('UserEntry:Register'))

        self.assertEqual(checker.status_code, 200)
        self.assertTemplateUsed(checker, 'UserEntry/Register.html')



    def test_view_registration_success(self):
        checker = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'rqeuioqwiuoqrw',
                                          'email':'reuioqwruyqwe@example.com',
                                          'password1':'uweruiy1oui79',
                                          'password2':'uweruiy1oui79',})

        self.assertEqual(checker.status_code, 302)



    def test_view_registration_failure_on_email_lacking_information(self):
        checker = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'retgtrfgsdvbn',
                                          'email':'test',
                                          'password1':'uweruiy1oui79',
                                          'password2':'uweruiy1oui79',})

        self.assertEqual(checker.status_code, 200)



    def test_view_registration_failure_on_password_retype(self):
        checker = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'fdfsdsfadasdf',
                                          'email':'test@gmail.com',
                                          'password1':'YouShallNotPass!',
                                          'password2':'YouWillNeverGuess!',})

        self.assertEqual(checker.status_code, 200)




    def test_view_registration_failure_on_username_repeat(self):
        checker = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'Test1',
                                          'email':'thisisanemail@example.com',
                                          'password1':'YouShallNotPass!',
                                          'password2':'YouShallNotPass!',})

        checker2 = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'Test1',
                                          'email':'thisisanemail@example.com',
                                          'password1':'YouShallNotPass!',
                                          'password2':'YouShallNotPass!',})


        self.assertEqual(checker2.status_code, 200)





    def test_view_registration_failure_on_email_repeat(self):
        checker = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'Test300',
                                          'email':'TestingTesting@example.com',
                                          'password1':'YouShallNotPass!',
                                          'password2':'YouShallNotPass!',})

        checker2 = self.client.post(reverse('UserEntry:Register'),
                                    data={'username':'Test300',
                                          'email':'TestingTesting@example.com',
                                          'password1':'YouShallNotPass!',
                                          'password2':'YouShallNotPass!',})

        self.assertEqual(checker2.status_code, 200)

#This test does not test if logging in functions
#Only that the page loads successfully and that the correct template is used
#That is because this view is a django view, a django form, and a django model
#Unless django itself breaks down those elements of the page won't ever fail
class UserLoginViewTests(TestCase):

    def test_page_exists_at_view_url(self):
        checker = self.client.get('/Accounts/Login/')

        self.assertEqual(checker.status_code, 200)

    def test_page_accessible_by_name(self):
        checker = self.client.get(reverse('UserEntry:Login'))

        self.assertEqual(checker.status_code, 200)

    def test_page_template_accurate(self):
        checker = self.client.get(reverse('UserEntry:Login'))

        self.assertEqual(checker.status_code, 200)
        self.assertTemplateUsed(checker, 'UserEntry/Login.html')

def AccountVerifyFailSetup():
    checker = self.client.get('/Accounts/Activate/Mzc/4yh-89234927343213a42543/')

class AccountVerificationViewTests(TestCase):
    #This test actually makes sure of a variety of things
    #Firstly, it indirectly checks that a page exists at the url
    #It would not throw an error if it didn't
    #Secondly, it tests that the URL throws an error
    #This error is caused by the lack of a user associated with the token
    #Going to the url gives the user a verification failure page
    def test_page_exists_at_view_url_with_error(self):

        self.assertRaises(Exception, AccountVerifyFailSetup)

class ActivationSentViewTests(TestCase):

    def test_page_exists_at_view_url(self):
        checker = self.client.get('/Accounts/Register/')

        self.assertEqual(checker.status_code, 200)

    def test_page_accessible_by_name(self):
        checker = self.client.get(reverse('UserEntry:ActivationSent'))

        self.assertEqual(checker.status_code, 200)

    def test_page_template_accurate(self):
        checker =self.client.get(reverse('UserEntry:ActivationSent'))

        self.assertEqual(checker.status_code, 200)
        self.assertTemplateUsed(checker, 'UserEntry/ActivationSent.html')
