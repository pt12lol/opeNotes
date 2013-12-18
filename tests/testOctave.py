#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from src.octave import Octave
from copy import copy


class TestOctave(unittest.TestCase):

    def setUp(self):
        self.o1 = Octave()
        self.o2 = Octave(0)
        self.o3 = Octave(0, 'upper')
        self.o4 = Octave(1, 'upper')
        self.o5 = Octave(1, 'lower')

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
        self.assertTrue(self.o2 != self.o4)
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

    def testGe(self):
        self.assertGreaterEqual(self.o1, self.o2)
        self.assertTrue(self.o2 >= self.o3)
        self.assertTrue(self.o3 >= self.o4)
        self.assertTrue(self.o1 >= self.o5)
        self.assertFalse(self.o4 >= self.o5)

    def testAdd(self):
        tmp = copy(self.o1)
        tmp += 1
        self.assertEqual(tmp, Octave(2))
        self.assertEqual(tmp + 2, Octave(4, 'lower'))
        self.assertEqual(tmp + (-3), Octave(0, 'upper'))
        self.assertEqual(tmp + (-2), Octave(0, 'lower'))
        self.assertEqual(tmp + (-4), Octave(1, 'upper'))

    def testSub(self):
        tmp = copy(self.o1)
        tmp -= -1
        self.assertEqual(tmp, Octave(2))
        self.assertEqual(tmp - (-2), Octave(4, 'lower'))
        self.assertEqual(tmp - 3, Octave(0, 'upper'))
        self.assertEqual(tmp - 2, Octave(0, 'lower'))
        self.assertEqual(tmp - 4, Octave(1, 'upper'))
        self.assertEqual(tmp - Octave(0), 2)
        self.assertEqual(tmp - Octave(4), -2)

