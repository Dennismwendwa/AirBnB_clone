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
