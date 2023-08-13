#!/usr/bin/python3
"""These are the tests for FileStorage class"""

import os
import unittest
import json

from models.engine.file_storage import FileStorage
import models


class TestFilesStorage(unittest.TestCase):
    """This are tests for this class"""

    def test_attr(self):
        self._class = FileStorage
        self._name = "FileStorage"
        base = self._class()
        self.assertFalse(os.path.exists("file.json"))
        self.assertIsInstance(base.all(), dict)

    def test_save(self):
        pass

    def test_reload(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_new_method(self):
        pass

    def test_all_method(self):
        pass


if __name__ == "__main__":
    unittest.main()
