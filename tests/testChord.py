#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from opeNotes.pitch import Pitch
from opeNotes.interval import Interval
from opeNotes.chord import Chord


class TestChord(unittest.TestCase):

    def setUp(self):
        self.c1 = Chord()
        self.c1.intervals.append(Interval(3))
        self.c1.intervals.append(Interval(3, 'minor'))
        self.c2 = Chord()
        self.c2.intervals.append(Interval(3))
        self.c2.intervals.append(Interval(3, 'minor'))
        self.c2.intervals.append(Interval(3, 'minor'))
        self.c3 = Chord()
        self.c3.intervals.append(Interval(4))
        self.c3.intervals.append(Interval(4))
        self.c4 = Chord(Interval(3), Interval(3, 'minor'))

    def testRepr(self):
        self.assertEqual(str(self.c1), "[3, 3>]")
        self.assertEqual(str(self.c2), "[3, 3>, 3>]")
        self.assertEqual(str(self.c3), "[4, 4]")
        self.assertEqual(str(self.c4), "[3, 3>]")

    def testEq(self):
        self.assertEqual(self.c1, self.c4)
        self.assertTrue(self.c4 == self.c1)
        self.assertFalse(self.c2 == self.c4)
        self.assertFalse(self.c3 == self.c4)
        self.assertFalse(self.c1 == self.c3)

    def testNe(self):
        self.assertNotEqual(self.c1, self.c2)
        self.assertTrue(self.c2 != self.c3)
        self.assertTrue(self.c2 != self.c4)
        self.assertFalse(self.c1 != self.c4)

    def testBuildFrom(self):
        D = self.c1.buildFrom(Pitch('d'))
        self.assertTrue(Pitch('d') in D)
        self.assertTrue(Pitch('f', 2) in D)
        self.assertTrue(Pitch('a') in D)
        self.assertEqual(len(D), 3)
        Fis7 = self.c2.buildFrom(Pitch('f', 2))
        self.assertTrue(Pitch('f', 2) in Fis7)
        self.assertTrue(Pitch('a', 2) in Fis7)
        self.assertTrue(Pitch('c', 2, 2) in Fis7)
        self.assertTrue(Pitch('e', 0, 2) in Fis7)
        self.assertEqual(len(Fis7), 4)

