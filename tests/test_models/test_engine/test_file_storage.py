#!/usr/bin/python3
"""These are the tests for FileStorage class"""

import os
import unittest
import json

from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFilesStorage(unittest.TestCase):
    """This are tests for this class"""

    def test_attr(self):
        self._class = FileStorage
        self._name = "FileStorage"
        base = self._class()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIsInstance(base.all(), dict)
    
    def test_new(self):
        Base = BaseModel()
        Usr = User()
        Sta = State()
        Plac = Place()
        Ciy = City()
        Amen = Amenity()
        Revi = Review()
        
        models.storage.new(Base)
        models.storage.new(Usr)
        models.storage.new(Sta)
        models.storage.new(Plac)
        models.storage.new(Ciy)
        models.storage.new(Amen)
        models.storage.new(Revi)

        self.assertIn("BaseModel." + Base.id, models.storage.all().keys())
        self.assertIn(Base, models.storage.all().values())

        self.assertIn("User." + Usr.id, models.storage.all().keys())
        self.assertIn(Usr, models.storage.all().values())

        self.assertIn("State." + Sta.id, models.storage.all().keys())
        self.assertIn(Sta, models.storage.all().values())

        self.assertIn("Place." + Plac.id, models.storage.all().keys())
        self.assertIn(Plac, models.storage.all().values())

        self.assertIn("City." + Ciy.id, models.storage.all().keys())
        self.assertIn(Ciy, models.storage.all().values())

        self.assertIn("Amenity." + Amen.id, models.storage.all().keys())
        self.assertIn(Amen, models.storage.all().values())

        self.assertIn("Review." + Revi.id, models.storage.all().keys())
        self.assertIn(Revi, models.storage.all().values())
    
    def test_save(self):
        Base = BaseModel()
        Usr = User()
        Sta = State()
        Plac = Place()
        Ciy = City()
        Amen = Amenity()
        Revi = Review()

        models.storage.new(Base)
        models.storage.new(Usr)
        models.storage.new(Sta)
        models.storage.new(Plac)
        models.storage.new(Ciy)
        models.storage.new(Amen)
        models.storage.new(Revi)
        models.storage.save()
        save_massage = ""
        with open("file.json", "r") as file:
            save_massage = file.read()
            self.assertIn("BaseModel." + Base.id, save_massage)
            self.assertIn("User." + Usr.id, save_massage)
            self.assertIn("State." + Sta.id, save_massage)
            self.assertIn("Place." + Plac.id, save_massage)
            self.assertIn("City." + Ciy.id, save_massage)
            self.assertIn("Amenity." + Amen.id, save_massage)
            self.assertIn("Review." + Revi.id, save_massage)
    
    def test_reload(self):
        Base = BaseModel()
        Usr = User()
        Sta = State()
        Plac = Place()
        Ciy = City()
        Amen = Amenity()
        Revi = Review()

        models.storage.new(Base)
        models.storage.new(Usr)
        models.storage.new(Sta)
        models.storage.new(Plac)
        models.storage.new(Ciy)
        models.storage.new(Amen)
        models.storage.new(Revi)
        models.storage.reload()
        objectss = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + Base.id, objectss)
        self.assertIn("User." + Usr.id, objectss)
        self.assertIn("State." + Sta.id, objectss)
        self.assertIn("Place." + Plac.id, objectss)
        self.assertIn("City." + Ciy.id, objectss)
        self.assertIn("Amenity." + Amen.id, objectss)
        self.assertIn("Review." + Revi.id, objectss)
    
    def test_new_using_kwargs(self):
        with self.assertRaises(TypeError):
            models.storage.new(User(), 1)

    def test_new_using_args(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_reload_from_storage(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_all_using_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_save_using_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_all_method(self):
        self.assertEqual(dict, type(models.storage.all()))


if __name__ == "__main__":
    unittest.main()
