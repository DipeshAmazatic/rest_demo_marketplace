from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class EmailActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    generate email verification token
    """
    def _make_hash_value(self, user, timestamp):
        """
        hash value
        """
        return (text_type(user.pk) + text_type(timestamp)) +  text_type(user.is_email_verified)
email_verified_token = EmailActivationTokenGenerator()