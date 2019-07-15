#Non project imports
import unittest

#Project imports
from UserEntry import urls
from UserEntry.tokens import AccountActivationToken

class FakeUserSetUp():
    pk = 1
    is_active = False

#These tests are for the token generator used in user validation URLs
class TokenCreationTests(unittest.TestCase):

    def test_token_generator_exists(self):
        SetUp = FakeUserSetUp()
        Checker = AccountActivationToken.make_token(SetUp)

        self.assertFalse(0, Checker)

    #This test requires that the token generator is not changed
    #If the token generator outputs tokens of a different kind to its initial creation
    #EG: Switches to a SHA256 hash generator, bases the token on different variables, ect
    #Then this test will break
    def test_token_generator_output_correct(self):
        SetUp = FakeUserSetUp()
        Checker = AccountActivationToken.make_token(SetUp)

        self.assertEqual('4yh-33b9ac27ecd8e9ba4ffc', Checker)
