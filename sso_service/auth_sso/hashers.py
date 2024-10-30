from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.conf import settings

class CustomPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    def encode(self, password, salt, iterations=None):
        secret_key = settings.SECRET_KEY  # Use each app's secret key
        password = f"{password}{secret_key}"
        return super().encode(password, salt, iterations)

    def verify(self, password, encoded):
        secret_key = settings.SECRET_KEY
        password = f"{password}{secret_key}"
        return super().verify(password, encoded)
