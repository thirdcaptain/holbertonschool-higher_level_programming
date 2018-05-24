#!/usr/bin/python3
"""Unittest for Base class
"""

import pep8
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_1_id(self):
        """ test base id increment and setting
        """
        Base.reset()
        b1 = Base()
        b2 = Base()
        b5 = Base(5)
        bcow = Base("cow")
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b5.id, 5)
        self.assertEqual(bcow.id, "cow")
        self.assertEqual(b3.id, 3)

    def test_2_pep8_test(self):
        """Tests for pep8 in test_base
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix test_base.py pep8")

    def test_3_pep8_models(self):
        """Tests for pep8 in models
        """
        p8 = pep8.StyleGuide(quiet=True)
        b = p8.check_files(['models/base.py'])
        self.assertEqual(b.total_errors, 0, "fix base.py pep8")

    def test_4_docstring(self):
        """Tests for docstring
        """
        self.assertIsNotNone(Base.__doc__)

    def test_5_doc_methods(self):
        """Tests all methods for docstrings
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "reset"))
        self.assertTrue(Base.reset.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.load_from_file.__doc__)

    def test_6_to_json_string(self):
        """Tests to_json_string
        """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_7_from_json_string(self):
        """Tests from_json_string
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        s = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}, \
{"id": 10, "width": 12, "height": 14, "x": 16, "y": 18}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

        if __name__ == 'main':
            unittest.main()
