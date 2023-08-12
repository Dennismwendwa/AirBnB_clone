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
import models

import unittest
import sys
from io import StringIO
from unittest.mock import patch
import tempfile
import os


class TestHBNBCommandPrompt(unittest.TestCase):
    """Testing for HBNBCommand prompt"""

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


class TestHBNBCommand_quit(unittest.TestCase):
    """This class tests quit and EOF"""

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
        self.tempfile = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        self.mock_stdout.close()
        os.remove(self.tempfile.name)

    def test_help_quit(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("help quit")
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("Quit command to exit the program", output)
    
    def test_help(self):
        message = ("Documented commands (type help <topic>):\n"
                   "========================================\n"
                   "EOF  all  create  destroy  help  quit  show  update")
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
                   "Usage: show <class name> <instance id>")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_destroy(self):
        message = ("Deletes an instance based on the class name and id\n        "
                   "Usage: destroy <class name> <instance id>")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_all(self):
        message = ("Prints all string representation of all instances based or\n        "
                   "not on the class name.\n        "
                   "Args:\n            "
                   "arg (str): Class name")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_update(self):
        message = ("Updates an instance based on the class name and id by adding or\n        "
                   "updating attribute\n        "
                   "Usage: update <class name> <instance id> <attribute name>\n        "
                   '"<attribute value>"')
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertIn(message, f.getvalue().strip())


class TestCreateCommand(unittest.TestCase):
    """This class is testing the create command"""

    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()
        self.tempfile = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        self.mock_stdout.close()
        os.remove(self.tempfile.name)

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
        message = "*** Unknown syntax: tony"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("tony"))
            self.assertEqual(message, f.getvalue().strip())


class TestShowCommand(unittest.TestCase):
    """These are the test for do_show command"""

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.mock_stdout = StringIO()
        self.tempfile = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        self.mock_stdout.close()
        self.tempfile.close()
        os.remove(self.tempfile.name)

    def test_valid_show_basemodel(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_valid_show_user(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create User")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show User {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_valid_show_state(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create State")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show State {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_valid_show_city(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create City")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show City {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_valid_show_amenity(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create Amenity")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show Amenity {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_valid_show_place(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create Place")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show Place {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_valid_show_review(self):
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create Review")
            object_id = self.mock_stdout.getvalue().strip()

        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(f"show Review {object_id}")
            self.assertIn(object_id, self.mock_stdout.getvalue().strip())

    def test_show_unknow_classneme(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show NoClassName")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_classname(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_basemodel(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show BaseModel")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_user(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show User")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_state(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show State")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_city(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show City")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_amenity(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Amenity")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_place(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Place")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_no_id_review(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Review")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_basemodel(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show BaseModel 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_user(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show User 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show State 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show City 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Amenity 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Place 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Review 777")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_basemodel(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("BaseModel.show(44)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_user(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("User.show(777)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("State.show(777)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_city(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("City.show(777)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_amenity(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Amenity.show(777)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_place(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Place.show(777)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_invalid_id_dot_lookup_review(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Review.show(777)")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_basemodel(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("BaseModel.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_lookup_user(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("User.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_state(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("State.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_lookup(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("City.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_lookup_amenity(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Amenity.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_lookup_place(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Place.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_missing_dot_lookup_Review(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Review.show()")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_basemodel(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show BaseModel")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_user(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show User")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_state(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show State")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_city(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show City")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_amenity(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Amenity")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_place(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Place")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_instance_id_misssing_positionkeyword_lookup_review(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show Review")
            self.assertEqual(message, self.mock_stdout.getvalue().strip())

    def test_show_basemodel_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["BaseModel.{}".format(lookup)]
            cmd = "BaseModel.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())

    def test_show_user_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["User.{}".format(lookup)]
            cmd = "User.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())

    def test_show_state_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["State.{}".format(lookup)]
            cmd = "State.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())

    def test_show_city_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["City.{}".format(lookup)]
            cmd = "City.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())

    def test_show_amenity_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Amenity.{}".format(lookup)]
            cmd = "Amenity.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())

    def test_show_place_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(" create Place"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Place.{}".format(lookup)]
            cmd = "Place.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())

    def test_show_review_attri(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            lookup = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Review.{}".format(lookup)]
            cmd = "Review.show({})".format(lookup)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objec.__str__(), f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
