#!/usr/bin/python3
"""
For the BaseModel class unit tests
"""

import os
import unittest
import datetime
import json
import pycodestyle
from models.base_model import BaseModel
import inspect  # Add missing import for inspect


class TestBaseModel(unittest.TestCase):
    """
    Case tests for the BaseModel class
    """

    def setUp(self):
        """Before every test make sure area is tidy."""
        pass

    def tearDown(self):
        """After each test tidy up the resources."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pycodestyle(self):
        """
        Test whether base_model file complies with PEP 8.
        """
        pycodestyle_checker = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyle_checker.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP 8 style errors (and warnings).")

    def test_create_default_instance(self):
        """
        Verify that BaseModel is created in default instance.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_create_instance_from_dict(self):
        """
        Use the 'to_dict' method to test instance creation process.
        """
        original_instance = BaseModel()
        original_copy = original_instance.to_dict()
        new_instance = BaseModel(**original_copy)
        self.assertIsNot(new_instance, original_instance)

    def test_create_instance_invalid_args(self):
        """
        Try starting an instance with incorrect parameters.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        instance_dict.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**instance_dict)

    def test_save_method(self):
        """
        Examine precision of saved data and the 'save' method.
        """
        instance = BaseModel()
        instance.save()
        key = f'{instance.__class__.__name__}.{instance.id}'
        with open('file.json', 'r') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data[key], instance.to_dict())

    def test_str_representation(self):
        """
        Use the __str__ method to see if representation is readable.
        """
        instance = BaseModel()
        expected_str = f'[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_str)

    def test_to_dict_method(self):
        """
        Examine 'to_dict' function.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance.to_dict(), instance_dict)

    def test_id_type(self):
        """
        Verify the 'id' attributes type.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.id, str)

    def test_created_at_type(self):
        """
        Verify the 'created_at' attributes type.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """
        The 'updated_at' attribute and how it relates to the 'created_at'.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.updated_at, datetime.datetime)
        instance_dict = new_instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertNotEqual(new_instance.created_at, new_instance.updated_at)

    def test_uuid_generation(self):
        """
        Test the process of creating distinct UUIDs.
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        list_instances = [instance1, instance2, instance3]
        for instance in list_instances:
            with self.subTest(uuid=instance.id):
                self.assertIsInstance(instance.id, str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """
        In order to get readable representation try the __str__ method.
        """
        instance = BaseModel()
        expected_str = f'[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_str)


if __name__ == "__main__":
    unittest.main()
