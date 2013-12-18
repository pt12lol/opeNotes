#!/usr/bin/pythpn
# -*- cpding: utf-8 -*-

import unittest
from src.pitch import Pitch, Octave
from copy import copy


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.p1 = Pitch()
        self.p2 = Pitch('d', 2, 0)
        self.p3 = Pitch.fromOctave('c', -3, Octave(0))
        self.p4 = Pitch('b', 4, 0, 'upper')
        self.p5 = Pitch('a', 0, 1, 'lower')
        self.p6 = Pitch.fromOctave('c', 1, Octave(0))

    def testRepr(self):
        self.assertEqual(str(self.p1), "a'")
        self.assertEqual(str(self.p2), "dis")
        self.assertEqual(str(self.p3), "ceseh")
        self.assertEqual(str(self.p4), "bisis,")
        self.assertEqual(str(self.p5), "a'")

    def testEq(self):
        self.assertEqual(self.p1, self.p5)
        self.assertTrue(self.p1 == self.p5)
        self.assertFalse(self.p2 == self.p4)
        self.assertFalse(self.p3 == self.p4)
        self.assertFalse(self.p3 == self.p5)

    def testNe(self):
        self.assertNotEqual(self.p1, self.p2)
        self.assertTrue(self.p2 != self.p3)
        self.assertTrue(self.p2 != self.p4)
        self.assertFalse(self.p1 != self.p5)

    def testLt(self):
        self.assertLess(self.p2, self.p1)
        self.assertTrue(self.p3 < self.p2)
        self.assertTrue(self.p4 < self.p3)
        self.assertFalse(self.p5 < self.p4)
        self.assertFalse(self.p1 < self.p5)
        self.assertFalse(self.p6 < self.p3)

    def testGt(self):
        self.assertGreater(self.p1, self.p2)
        self.assertTrue(self.p2 > self.p3)
        self.assertTrue(self.p3 > self.p4)
        self.assertFalse(self.p4 > self.p5)
        self.assertFalse(self.p1 > self.p5)
        self.assertFalse(self.p3 > self.p6)

    def testLe(self):
        self.assertLessEqual(self.p2, self.p1)
        self.assertLessEqual(self.p5, self.p1)
        self.assertTrue(self.p3 <= self.p2)
        self.assertTrue(self.p4 <= self.p3)
        self.assertTrue(self.p1 <= self.p5)
        self.assertFalse(self.p5 <= self.p4)
        self.assertFalse(self.p6 <= self.p3)

    def testGe(self):
        self.assertGreaterEqual(self.p1, self.p2)
        self.assertTrue(self.p2 >= self.p3)
        self.assertTrue(self.p3 >= self.p4)
        self.assertTrue(self.p1 >= self.p5)
        self.assertFalse(self.p4 >= self.p5)
        self.assertFalse(self.p3 >= self.p6)

