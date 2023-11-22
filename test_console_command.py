#!/usr/bin/python3

import unittest
import MySQLdb

class TestConsoleCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Establish a connection to the MySQL test database.
        cls.db = MySQLdb.connect(
            host="localhost",
            user="hbnb_test",
            passwd="hbnb_test_pwd",
            db="hbnb_test_db"
        )
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the MySQL database connection
        cls.db.close()

    def test_create_state_command(self):
        # Obtain the starting count of entries in the "states" table.
        initial_count = self.get_records_count()

        # Execute the console command (replace with actual command execution)
        # console_command.create_state(name="California")

        # Obtain the updated record count in the 'states' table.
        new_count = self.get_records_count()

        # Verify the tests validity.
        self.assertEqual(new_count, initial_count + 1, "State creation test failed")

    def get_records_count(self):
        # Many records are there in the 'states' table.
