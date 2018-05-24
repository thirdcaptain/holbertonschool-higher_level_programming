#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_class(self):
        Base.reset()
        c = Base()
        self.assertEqual(c.id, 1)

    def test_id(self):
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

    if __name__ == 'main':
        unittest.main()
