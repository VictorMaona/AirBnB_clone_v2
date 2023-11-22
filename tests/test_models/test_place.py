#!/usr/bin/python3
"""Place class test module"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """Example cases for the Place class"""

    def __init__(self, *args, **kwargs):
        """Set up the TestPlace class initially."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Verify whether 'city_id' attribute is of string type.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Verify the 'user_id' attribute string type.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Verify the 'name' property is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Verify the 'description' property is a string.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Check to see 'number_rooms' attribute is an int.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Check to 'number_bathrooms' attr is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Verify the 'max_guest' attribute is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Checks the 'price_by_night' attr is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Test if the 'latitude' attribute is of type float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test 'longitude' attr is of the float type.
        """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """
        Verify the attr 'amenity_ids' is of type list.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
