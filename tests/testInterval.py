#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from opeNotes.interval import Interval


class TestInterval(unittest.TestCase):

    def setUp(self):
        self.i1 = Interval(3)
        self.i2 = Interval(5, 'up', 'perfect')
        self.i3 = Interval(7)
        self.i4 = Interval(7, type_='minor')
        self.i5 = Interval(4, 'down', 'aug', 1)
        self.i6 = Interval(3, 'up', 'major')
        self.i7 = Interval(10, 'down', 'minor')

    def testRepr(self):
        self.assertEqual(str(self.i1), "3")
        self.assertEqual(str(self.i2), "5")
        self.assertEqual(str(self.i3), "7<")
        self.assertEqual(str(self.i4), "7")
        self.assertEqual(str(self.i5), "4<")
        self.assertEqual(str(self.i6), "3")
        self.assertEqual(str(self.i7), "10>")

    def testEq(self):
        self.assertEqual(self.i1, self.i6)
        self.assertTrue(self.i6 == self.i1)
        self.assertFalse(self.i2 == self.i4)
        self.assertFalse(self.i3 == self.i4)
        self.assertFalse(self.i7 == self.i5)

    def testNe(self):
        self.assertNotEqual(self.i1, self.i2)
        self.assertTrue(self.i2 != self.i3)
        self.assertTrue(self.i2 != self.i4)
        self.assertFalse(self.i1 != self.i6)

