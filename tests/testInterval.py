#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from opeNotes.interval import Interval


class TestInterval(unittest.TestCase):

    def setUp(self):
        self.i1 = Interval(3)
        self.i2 = Interval(5, 'perfect')
        self.i3 = Interval(7)
        self.i4 = Interval(7, 'minor')
        self.i5 = Interval(-4, 'aug', 1)
        self.i6 = Interval(3, 'major')
        self.i7 = Interval(-10, 'minor')

    def testRepr(self):
        self.assertEqual(str(self.i1), "3")
        self.assertEqual(str(self.i2), "5")
        self.assertEqual(str(self.i3), "7<")
        self.assertEqual(str(self.i4), "7")
        self.assertEqual(str(self.i5), "-4<")
        self.assertEqual(str(self.i6), "3")
        self.assertEqual(str(self.i7), "-10>")

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

    def testSemitones(self):
        self.assertEqual(self.i1.semitones(), 4)
        self.assertEqual(self.i2.semitones(), 7)
        self.assertEqual(self.i3.semitones(), 11)
        self.assertEqual(self.i4.semitones(), 10)
        self.assertEqual(self.i5.semitones(), -6)
        self.assertEqual(self.i6.semitones(), 4)
        self.assertEqual(self.i7.semitones(), -15)

    def testNeg(self):
        self.assertEqual(-self.i1, Interval(-3))
        self.assertEqual(-self.i2, Interval(-5))
        self.assertEqual(-self.i3, Interval(-7))
        self.assertEqual(-self.i5, Interval(4, 'aug'))
        self.assertEqual(-self.i7, Interval(10, 'minor'))

    def testInversion(self):
        self.assertEqual(self.i1.inversion(), Interval(6, 'minor'))
        self.assertEqual(self.i2.inversion(), Interval(4))
        self.assertEqual(self.i3.inversion(), Interval(2, 'minor'))
        self.assertEqual(self.i5.inversion(), Interval(-5, 'dim', 1))
        self.assertEqual(self.i7.inversion(), Interval(-6))

