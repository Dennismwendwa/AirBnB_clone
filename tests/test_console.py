#!/usr/bin/python3
"""
This are the test for console module

"""
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import unittest
import sys
from io import StringIO
from unittest.mock import patch


class TestHBNBCommandPrompt(unittest.TestCase):
    """Testing for HBNBCommand prompt"""
    
    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


class TestHBNBCommand_quit(unittest.TestCase):
    """These class tests quit and EOF"""

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()
    
    def test_quit_command(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual("", self.mock_stdout.getvalue().strip())

    def test_EOF_command(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual("", self.mock_stdout.getvalue().strip())


class TestHelpForAllMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    def test_help_quit(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("help quit")
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("Quit command to exit the program", output)
    
    def test_help(self):
        message = ("Documented commands (type help <topic>):\n"
                   "========================================\n"
                   "EOF  all  create  destroy  help  quit  show  update"
                )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(message, f.getvalue().strip())
    
    def test_help_EOF(self):
        message = "Exits the program without crashing"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(message, output.getvalue().strip())

    def test_help_create(self):
        message = "Creates a new instance of BaseModel, saves it (to the JSON file)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertIn(message, output.getvalue().strip())

    def test_help_show(self):
        message = ("Prints the string representation of an instance\n        "
                   "based on the class name and id\n        "
                   "Usage: show <class name> <instance id>"
                   )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_destroy(self):
        message = ("Deletes an instance based on the class name and id\n        "
                   "Usage: destroy <class name> <instance id>"
                )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_all(self):
        message = ("Prints all string representation of all instances based or\n        "
                   "not on the class name.\n        "
                   "Args:\n            "
                   "arg (str): Class name"
                )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_update(self):
        message = ("Updates an instance based on the class name and id by adding or\n        "
                   "updating attribute\n        "
                   "Usage: update <class name> <instance id> <attribute name>\n        "
                   '"<attribute value>"'
                )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertIn(message, f.getvalue().strip())



class TestCreateCommand(unittest.TestCase):
    """This class is testing the create command"""

    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    def test_create_valid_basemodel(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

    
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show BaseModel {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_create_valid_User(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create User")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show User {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_create_valid_State(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create State")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show State {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)


    def test_create_valid_City(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create City")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show City {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_create_valid_Amenity(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create Amenity")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Amenity {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_create_valid_Place(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create Place")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Place {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_create_valid_Review(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create Review")
            output = self.mock_stdout.getvalue().strip()
            object_id = output
            self.assertTrue(len(output) == 36)

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Review {}".format(object_id))
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("'id': '{}'".format(object_id), output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_create_invalid_class(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create InvalidCalssTony")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_create_missing_class(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual("** class name missing **", output)

    def test_create_unkwow_stntax(self):
        message ="*** Unknown syntax: tony"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("tony"))
            self.assertEqual(message, f.getvalue().strip())
















