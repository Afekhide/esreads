from unittest import TestCase
from esreads.models.user import User


class UserTestCase(TestCase):
    def test_password_hash(self):
        user = User(password='Goat')
        self.assertFalse(user.password_hash is None)

    def test_password_readonly(self):
        user = User(password='random')
        with self.assertRaises(AttributeError):
            print(user.password)

    def test_different_hashes(self):
        user1 = User(password='password')
        user2 = User(password='password')
        self.assertFalse(user1.password_hash is user2.password_hash)

    def test_verify_password(self):
        user = User(password='random')
        self.assertTrue(user.verify_password('random'))
        self.assertFalse(user.verify_password('randomly'))

    def test_password_hashed(self):
        user = User(password='random')
        self.assertTrue(user.password_hash.startswith('pbkdf2:sha256:'))

