from django.test import TestCase
from .hashers import CustomPBKDF2PasswordHasher

class CustomPasswordHasherTest(TestCase):
    def setUp(self):
        self.password = "secure_password"
        self.hasher = CustomPBKDF2PasswordHasher()

    def test_hash_password(self):
        # Test password hashing
        hashed = self.hasher.encode(self.password)
        self.assertIsNotNone(hashed)

    def test_verify_password(self):
        # Hash the password first
        hashed = self.hasher.encode(self.password)
        # Verify it
        self.assertTrue(self.hasher.verify(self.password, hashed))

    def test_verify_incorrect_password(self):
        # Hash the password
        hashed = self.hasher.encode(self.password)
        # Verify a wrong password
        self.assertFalse(self.hasher.verify("wrong_password", hashed))
        
    def test_validate_password(self):
        app_key = "my_secret_key"  # Example app key
        stored_hash = self.hasher.encode(self.password, app_key)
        self.assertTrue(validate_password(app_key, self.password, stored_hash))
        self.assertFalse(validate_password(app_key, "wrong_password", stored_hash))
