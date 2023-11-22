#!/usr/bin/python3
"""
For the BaseModel class unit tests
"""

from models.base_model import BaseModel
import unittest
import datetime
import json
import os
import pycodestyle
import inspect  # Add missing import for inspect


class TestBaseModel(unittest.TestCase):
    """
    The BaseModel class test cases
    """

    def setUp(self):
        """Prepare spotless atmosphere for each test."""
        pass

    def tearDown(self):
        """After every test tidy up the resources."""
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

    def test_default_instance(self):
        """
        Check that default instance is created.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_copy_instance(self):
        """
        Test 'to_dict' method creation of an instance.
        """
        original_instance = BaseModel()
        original_copy = original_instance.to_dict()
        new_instance = BaseModel(**original_copy)
        self.assertIsNot(new_instance, original_instance)

    def test_copy_instance_invalid_args(self):
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
        Verify accuracy of data saved and the save technique.
        """
        instance = BaseModel()
        instance.save()
        key = f'{instance.__class__.__name__}.{instance.id}'
        with open('file.json', 'r') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data[key], instance.to_dict())

    def test_str_representation(self):
        """
        The __str__ method to see if representation is readable.
        """
        instance = BaseModel()
        expected_str = f'[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_str)

    def test_to_dict_method(self):
        """
        Try out the to_dict technique.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance.to_dict(), instance_dict)

    def test_id_type(self):
        """
        Verify the 'id' attribute type.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.id, str)

    def test_created_at_type(self):
        """
        Verify the 'created_at' attribute type.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """
        Verify 'updated_at' attribute type and connection to 'created_at'.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.updated_at, datetime.datetime)
        instance_dict = new_instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertNotEqual(new_instance.created_at, new_instance.updated_at)

    def test_uuid_generation(self):
        """
        Verify the creation of distinct UUIDs.
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
        Use the __str__ method to see if representation is readable.
        """
        instance = BaseModel()
        expected_str = f'[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_str)


if __name__ == "__main__":
    unittest.main()
