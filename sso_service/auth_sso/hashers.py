from django.contrib.auth.hashers import BasePasswordHasher
from hashlib import pbkdf2_hmac
import os

class CustomPBKDF2PasswordHasher(BasePasswordHasher):
    algorithm = "pbkdf2_sha256"
    iterations = 100000

    def _hash(self, password, salt):
        return pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), self.iterations)

    def encode(self, password, salt=None):
        if salt is None:
            salt = os.urandom(16).hex()
        hashed_password = self._hash(password, salt)
        return f"{self.algorithm}${self.iterations}${salt}${hashed_password.hex()}"

    def verify(self, password, encoded):
        algorithm, iterations, salt, hash = encoded.split('$')
        return self._hash(password, salt) == bytes.fromhex(hash)
        
    def validate_password(app_key, password, stored_hash):
        hasher = CustomPBKDF2PasswordHasher()
        return hasher.verify(password, stored_hash)
