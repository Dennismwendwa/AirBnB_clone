#!/usr/bin/python3
"""This are the test for console module"""
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
from models.engine.file_storage import FileStorage

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
        message = "Creates instance of BaseModel, saves it (to the JSON file)"
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
        message = ("Deletes an instance based the class name and id\n        "
                   "Usage: destroy <class name> <instance id>")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_all(self):
        message = ("Prints string representation instances based or\n        "
                   "not on the class name.\n        "
                   "Args:\n            "
                   "arg (str): Class name")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertIn(message, f.getvalue().strip())

    def test_help_update(self):
        message = "Updates instance based the class name adding or"
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


class TestDestroyCommand(unittest.TestCase):
    """This class tests destroy method"""

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.mock_stdout = StringIO()
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        self.mock_stdout.close()
        self.temp_file.close()

    def test_destroy_with_missing_class_name(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalid_class_name(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy InvalidClass")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_basemodel(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("BaseModel.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_user(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("User.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_state(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("State.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_city(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("City.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_amenity(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Amenity.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_place(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Place.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_dot_lookup_review(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Review.destroy()")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_basemodel(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_user(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy User")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_state(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy State")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_city(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy City")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_amenity(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy Amenity")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_place(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy Place")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_missingId_space_lookup_review(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy Review")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_basemodel(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy BaseModel 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_user(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy User 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy State 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_city(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy City 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_amenity(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy Amenity 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_place(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy Place 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_space_lookup_review(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy Review 88")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_basemodel(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("BaseModel.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_user(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("User.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_state(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("State.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_city(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("City.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_amenity(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Amenity.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_place(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Place.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_invalidId_dot_lookup_review(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("Review.destroy(88)")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(message, output)

    def test_destroy_with_valid_id_space_lookup_basemodel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["BaseModel.{}".format(obj_id)]
            cmd_h = "destroy BaseModel {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_space_lookup_user(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["User.{}".format(obj_id)]
            cmd_h = "destroy User {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_space_lookup_state(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["State.{}".format(obj_id)]
            cmd_h = "destroy State {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_space_lookup_city(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["City.{}".format(obj_id)]
            cmd_h = "destroy City {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_space_lookup_amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Amenity.{}".format(obj_id)]
            cmd_h = "destroy Amenity {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_space_lookup_place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Place.{}".format(obj_id)]
            cmd_h = "destroy Place {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_space_lookup_review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Review.{}".format(obj_id)]
            cmd_h = "destroy Review {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_basemodel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Review.{}".format(obj_id)]
            cmd_h = "BaseModel.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_user(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["User.{}".format(obj_id)]
            cmd_h = "User.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_state(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["State.{}".format(obj_id)]
            cmd_h = "State.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_city(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["City.{}".format(obj_id)]
            cmd_h = "City.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Amenity.{}".format(obj_id)]
            cmd_h = "Amenity.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Place.{}".format(obj_id)]
            cmd_h = "Place.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())

    def test_destroy_with_valid_id_dot_lookup_review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objec = models.storage.all()["Review.{}".format(obj_id)]
            cmd_h = "Review.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(cmd_h))
            self.assertNotIn(objec, models.storage.all())


class TestAllCommand(unittest.TestCase):
    """These are the tests for all command"""
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def test_all_no_class(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all InValid"))
            self.assertEqual(message, f.getvalue().strip())

    def test_all_no_class_dot_lookup(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BadClass.all()"))
            self.assertEqual(message, f.getvalue().strip())

    def test_all_dot_lookup_basemodel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[BaseModel] (", lines[0])

    def test_all_dot_lookup_user(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[User] (", lines[0])

    def test_all_dot_lookup_state(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[State] (", lines[0])

    def test_all_dot_lookup_city(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[City] (", lines[0])

    def test_all_dot_lookup_amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[Amenity] (", lines[0])

    def test_all_dot_lookup_place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[Place] (", lines[0])

    def test_all_dot_lookup_review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[Review] (", lines[0])

    def test_all_space_lookup_basemodel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[BaseModel] (", lines[0])

    def test_all_space_lookup_user(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[User] (", lines[0])

    def test_all_space_lookup_state(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[State] (", lines[0])

    def test_all_space_lookup_city(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[City] (", lines[0])

    def test_all_space_lookup_amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[Amenity] (", lines[0])

    def test_all_space_lookup_place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[Place] (", lines[0])

    def test_all_space_lookup_review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            lines = f.getvalue().strip().split("\n")
            self.assertIn("[Review] (", lines[0])

    def test_all_object_space_lookup(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertNotIn("Review", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", f.getvalue().strip())
            self.assertNotIn("Review", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", f.getvalue().strip())
            self.assertNotIn("Review", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", f.getvalue().strip())
            self.assertNotIn("Review", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertNotIn("Review", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", f.getvalue().strip())
            self.assertNotIn("Review", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", f.getvalue().strip())
            self.assertNotIn("Amenity", f.getvalue().strip())

    def test_all_object_dot_lookup(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertNotIn("City", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", f.getvalue().strip())
            self.assertNotIn("City", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", f.getvalue().strip())
            self.assertNotIn("City", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())


class TestCountCommand(unittest.TestCase):
    """This are the tests for count"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "dennis")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("dennis", "file.json")
        except IOError:
            pass

    def test_noneclass(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("NoneClass.count()"))
            self.assertEqual("0", f.getvalue().strip())

    def test_count_feature(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", f.getvalue().strip())


class TestUpdateCommand(unittest.TestCase):
    """This are the tests for update method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "dennis")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.jon")
        except IOError:
            pass
        try:
            os.rename("dennis", "file.json")
        except IOError:
            pass

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def test_updateclass_no_class(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual(message, f.getvalue().strip())

        message = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(".update()"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_invalid_class(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Bad"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_no_id_space_lookup(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update User"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update State"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update City"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Amenity"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Place"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Review"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_no_id_dot_lookup(self):
        message = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("BaseModel.update()"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("User.update()"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("State.update()"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("City.update()"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("Amenity.update()"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("Place.update()"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("Review.update()"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_invalidd_space_lookup(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 33"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update User 33"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update State 33"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update City 33"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Amenity 33"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Place 33"))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Review 33"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_missing_value_space_lookup(self):
        message = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update BaseModel {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update User {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update State {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update City {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update Amenity {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update Place {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            out = "update Review {} name_attr".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(out))
            self.assertEqual(message, f.getvalue().strip())

    def test_valid_update_space_lookup(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            ob_id = f.getvalue().strip()
            lines = "update BaseModel {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["BaseModel.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create User"))
            ob_id = f.getvalue().strip()
            lines = "update User {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["User.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create State"))
            ob_id = f.getvalue().strip()
            lines = "update State {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["State.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create City"))
            ob_id = f.getvalue().strip()
            lines = "update City {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["City.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Amenity"))
            ob_id = f.getvalue().strip()
            lines = "update Amenity {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["Amenity.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Place"))
            ob_id = f.getvalue().strip()
            lines = "update Place {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["Place.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Review"))
            ob_id = f.getvalue().strip()
            lines = "update Review {} name_attr 'value_attr'".format(ob_id)
            self.assertFalse(HBNBCommand().onecmd(lines))
            tesc = models.storage.all()["Review.{}".format(ob_id)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

    def test_update_validid_dot_lookup(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            obId = f.getvalue().strip()
            lin = "BaseModel.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["BaseModel.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create User"))
            obId = f.getvalue().strip()
            lin = "User.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["User.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create State"))
            obId = f.getvalue().strip()
            lin = "State.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["State.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create City"))
            obId = f.getvalue().strip()
            lin = "City.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["City.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Amenity"))
            obId = f.getvalue().strip()
            lin = "Amenity.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["Amenity.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Place"))
            obId = f.getvalue().strip()
            lin = "Place.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["Place.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Review"))
            obId = f.getvalue().strip()
            lin = "Review.update({}, name_attr, 'value_attr')".format(obId)
            self.assertFalse(HBNBCommand().onecmd(lin))
            tesc = models.storage.all()["Review.{}".format(obId)].__dict__
            self.assertEqual("value_attr", tesc["name_attr"])


if __name__ == "__main__":
    unittest.main()
