#!/usr/bin/python3
"""Review class test module"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Case tests for the Review course"""

    def __init__(self, *args, **kwargs):
        """Set up the TestReview class initially."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """
        The 'place_id' attribute in review is of string type.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id_type(self):
        """
        The 'user_id' attr in Review is of the string type.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text_type(self):
        """
        The 'text' property in Review is the string type.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
