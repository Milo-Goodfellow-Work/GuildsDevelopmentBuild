#Non project imports
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

#Project imports


#Generate a token responsible for account activation
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

AccountActivationToken  = TokenGenerator()
