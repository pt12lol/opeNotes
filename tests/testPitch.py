#!/usr/bin/pythpn
# -*- cpding: utf-8 -*-


import unittest
from opeNotes.octave import Octave
from opeNotes.interval import Interval
from opeNotes.pitch import Pitch


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.p1 = Pitch()
        self.p2 = Pitch('a', 0, 0)
        self.p3 = Pitch.fromOctave('c', -3, Octave(0))
        self.p4 = Pitch('b', 4, 0, 'upper')
        self.p5 = Pitch('a', 0, 1, 'lower')
        self.p6 = Pitch.fromOctave('c', 1, Octave(0))
        self.p7 = Pitch('c', 2, 0)

    def testRepr(self):
        self.assertEqual(str(self.p1), "a'")
        self.assertEqual(str(self.p2), "a")
        self.assertEqual(str(self.p3), "ceseh")
        self.assertEqual(str(self.p4), "bisis,")
        self.assertEqual(str(self.p5), "a'")
        self.assertEqual(str(self.p6), "cih")
        self.assertEqual(str(self.p7), "cis")

    def testEq(self):
        self.assertEqual(self.p1, self.p5)
        self.assertEqual(self.p4, self.p7)
        self.assertTrue(self.p1 == self.p5)
        self.assertTrue(self.p7 == self.p4)
        self.assertFalse(self.p2 == self.p4)
        self.assertFalse(self.p3 == self.p4)
        self.assertFalse(self.p3 == self.p5)

    def testNe(self):
        self.assertNotEqual(self.p1, self.p2)
        self.assertTrue(self.p2 != self.p3)
        self.assertTrue(self.p2 != self.p4)
        self.assertFalse(self.p1 != self.p5)
        self.assertFalse(self.p4 != self.p7)

    def testLt(self):
        self.assertLess(self.p2, self.p1)
        self.assertTrue(self.p3 < self.p2)
        self.assertTrue(self.p3 < self.p4)
        self.assertFalse(self.p5 < self.p4)
        self.assertFalse(self.p1 < self.p5)
        self.assertFalse(self.p6 < self.p3)
        self.assertFalse(self.p4 < self.p7)

    def testGt(self):
        self.assertGreater(self.p1, self.p2)
        self.assertTrue(self.p2 > self.p3)
        self.assertTrue(self.p4 > self.p3)
        self.assertFalse(self.p4 > self.p5)
        self.assertFalse(self.p1 > self.p5)
        self.assertFalse(self.p3 > self.p6)
        self.assertFalse(self.p4 > self.p7)

    def testLe(self):
        self.assertLessEqual(self.p2, self.p1)
        self.assertLessEqual(self.p5, self.p1)
        self.assertLessEqual(self.p4, self.p7)
        self.assertTrue(self.p3 <= self.p2)
        self.assertTrue(self.p3 <= self.p4)
        self.assertTrue(self.p1 <= self.p5)
        self.assertFalse(self.p5 <= self.p4)
        self.assertFalse(self.p6 <= self.p3)

    def testGe(self):
        self.assertGreaterEqual(self.p1, self.p2)
        self.assertGreaterEqual(self.p4, self.p7)
        self.assertTrue(self.p2 >= self.p3)
        self.assertTrue(self.p4 >= self.p3)
        self.assertTrue(self.p1 >= self.p5)
        self.assertFalse(self.p4 >= self.p5)
        self.assertFalse(self.p3 >= self.p6)

    def testAdd(self):
        tmp = self.p2
        tmp += Interval(3)
        self.assertTrue(tmp.eqNames(Pitch('c', 2)))
        self.assertTrue((tmp + Interval(2, 'minor')).eqNames(Pitch('d')))
        self.assertTrue((tmp + Interval(4)).eqNames(Pitch('f', 2)))
        self.assertTrue((tmp + Interval(-5, 'aug')).eqNames(Pitch('f', 0, 0)))
        self.assertTrue((tmp + Interval(-2)).eqNames(Pitch('b', 0, 0)))

    def testSub(self):
        tmp = self.p2
        tmp -= Interval(-6, 'minor')
        self.assertTrue(tmp.eqNames(Pitch('f')))
        self.assertTrue((tmp - Interval(-2, 'minor')).eqNames(Pitch('g', -2)))
        self.assertTrue((tmp - Interval(-5, 'aug')).eqNames(Pitch('c', 2, 2)))
        self.assertTrue((tmp - Interval(10)).eqNames(Pitch('d', -2, 0)))
        self.assertTrue((tmp - Interval(2)).eqNames(Pitch('e', -2)))

