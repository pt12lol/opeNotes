#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from opeNotes.rhythmicValue import RhythmicValue


class TestRhythmicValue(unittest.TestCase):

    def setUp(self):
        self.rv1 = RhythmicValue()
        self.rv2 = RhythmicValue(8, 1)
        self.rv3 = RhythmicValue(8, 0)
        self.rv4 = RhythmicValue(16, 2)
        self.rv5 = RhythmicValue(4, 0)

    def testRepr(self):
        self.assertEqual(str(self.rv1), '4')
        self.assertEqual(str(self.rv2), '8.')
        self.assertEqual(str(self.rv3), '8')
        self.assertEqual(str(self.rv4), '16..')
        self.assertEqual(str(self.rv5), '4')

    def testEq(self):
        self.assertEqual(self.rv1, self.rv5)
        self.assertTrue(self.rv1 == self.rv5)
        self.assertFalse(self.rv2 == self.rv4)
        self.assertFalse(self.rv3 == self.rv4)
        self.assertFalse(self.rv3 == self.rv5)

    def testNe(self):
        self.assertNotEqual(self.rv1, self.rv2)
        self.assertTrue(self.rv2 != self.rv3)
        self.assertTrue(self.rv2 != self.rv4)
        self.assertFalse(self.rv1 != self.rv5)

    def testLt(self):
        self.assertLess(self.rv2, self.rv1)
        self.assertTrue(self.rv3 < self.rv2)
        self.assertTrue(self.rv4 < self.rv3)
        self.assertFalse(self.rv5 < self.rv4)
        self.assertFalse(self.rv1 < self.rv5)

    def testGt(self):
        self.assertGreater(self.rv1, self.rv2)
        self.assertTrue(self.rv2 > self.rv3)
        self.assertTrue(self.rv3 > self.rv4)
        self.assertFalse(self.rv4 > self.rv5)
        self.assertFalse(self.rv1 > self.rv5)

    def testLe(self):
        self.assertLessEqual(self.rv2, self.rv1)
        self.assertLessEqual(self.rv5, self.rv1)
        self.assertTrue(self.rv3 <= self.rv2)
        self.assertTrue(self.rv4 <= self.rv3)
        self.assertTrue(self.rv1 <= self.rv5)
        self.assertFalse(self.rv5 <= self.rv4)

    def testGe(self):
        self.assertGreaterEqual(self.rv1, self.rv2)
        self.assertTrue(self.rv2 >= self.rv3)
        self.assertTrue(self.rv3 >= self.rv4)
        self.assertTrue(self.rv1 >= self.rv5)
        self.assertFalse(self.rv4 >= self.rv5)

