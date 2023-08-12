#!/usr/bin/python3
"""
This are the test for console module

"""
from console import HBNBCommand

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
