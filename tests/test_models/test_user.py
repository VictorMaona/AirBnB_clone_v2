#!/usr/bin/python3
"""User class testing module"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Case studies for the User class"""

    def __init__(self, *args, **kwargs):
        """Set up the TestUser class initially."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """
        The Users 'first_name' attribute is of type string.
        """
        new_user = self.value()
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name_type(self):
        """
        the Users 'last_name' attribute is type string.
        """
        new_user = self.value()
        self.assertEqual(type(new_user.last_name), str)

    def test_email_type(self):
        """
        The Users 'email' attribute is of type string.
        """
        new_user = self.value()
        self.assertEqual(type(new_user.email), str)

    def test_password_type(self):
        """
        The Users 'password' attribute is of type string.
        """
        new_user = self.value()
        self.assertEqual(type(new_user.password), str)
