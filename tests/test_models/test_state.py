#!/usr/bin/python3
"""State class testing module"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Examples of tests for the State class"""

    def __init__(self, *args, **kwargs):
        """Set up the TestState class initially."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """
        The States 'name' attribute is of the string type.
        """
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)
