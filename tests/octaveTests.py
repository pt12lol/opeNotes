#!/usr/bin/python
# -*- coding: utf-8 -*-

import undopth
from octave import Octave
import redopth

from copy import copy
import unittest


class OctaveTests(unittest.TestCase):

    def setUp(self):
        self.o1 = Octave('lower', 1)
        self.o2 = Octave('lower', 0)
        self.o3 = Octave('upper', 0)
        self.o4 = Octave('upper', 1)
        self.o5 = Octave('lower', 1)

    def testRepr(self):
        self.assertEqual(str(self.o1), "'")
        self.assertEqual(str(self.o2), "")
        self.assertEqual(str(self.o3), ",")
        self.assertEqual(str(self.o4), ",,")
        self.assertEqual(str(self.o5), "'")

    def testEq(self):
        self.assertEqual(self.o1, self.o5)
        self.assertTrue(self.o1 == self.o5)
        self.assertFalse(self.o2 == self.o4)
        self.assertFalse(self.o3 == self.o4)
        self.assertFalse(self.o3 == self.o5)

    def testNe(self):
        self.assertNotEqual(self.o1, self.o2)
        self.assertTrue(self.o2 != self.o3)
        self.assertTrue(self.o2 <> self.o4)
        self.assertFalse(self.o1 != self.o5)

    def testLt(self):
        self.assertLess(self.o2, self.o1)
        self.assertTrue(self.o3 < self.o2)
        self.assertTrue(self.o4 < self.o3)
        self.assertFalse(self.o5 < self.o4)
        self.assertFalse(self.o1 < self.o5)

    def testGt(self):
        self.assertGreater(self.o1, self.o2)
        self.assertTrue(self.o2 > self.o3)
        self.assertTrue(self.o3 > self.o4)
        self.assertFalse(self.o4 > self.o5)
        self.assertFalse(self.o1 > self.o5)

    def testLe(self):
        self.assertLessEqual(self.o2, self.o1)
        self.assertLessEqual(self.o5, self.o1)
        self.assertTrue(self.o3 <= self.o2)
        self.assertTrue(self.o4 <= self.o3)
        self.assertTrue(self.o1 <= self.o5)
        self.assertFalse(self.o5 <= self.o4)


def runTests():
    unittest.main()


if __name__ == '__main__':
    runTests()

