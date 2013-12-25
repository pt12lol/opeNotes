#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from opeNotes.pitch import Pitch
from opeNotes.interval import Interval
from opeNotes.pitchesStructure import PitchesStructure


class TestPitchesStructure(unittest.TestCase):

    def setUp(self):
        self.ps1 = PitchesStructure()
        self.ps1.intervals.append(Interval(3))
        self.ps1.intervals.append(Interval(3, 'minor'))
        self.ps2 = PitchesStructure()
        self.ps2.intervals.append(Interval(3))
        self.ps2.intervals.append(Interval(3, 'minor'))
        self.ps2.intervals.append(Interval(3, 'minor'))
        self.ps3 = PitchesStructure()
        self.ps3.intervals.append(Interval(4))
        self.ps3.intervals.append(Interval(4))
        self.ps4 = PitchesStructure(Interval(3), Interval(3, 'minor'))

    def testRepr(self):
        self.assertEqual(str(self.ps1), "[3, 3>]")
        self.assertEqual(str(self.ps2), "[3, 3>, 3>]")
        self.assertEqual(str(self.ps3), "[4, 4]")
        self.assertEqual(str(self.ps4), "[3, 3>]")

    def testEq(self):
        self.assertEqual(self.ps1, self.ps4)
        self.assertTrue(self.ps4 == self.ps1)
        self.assertFalse(self.ps2 == self.ps4)
        self.assertFalse(self.ps3 == self.ps4)
        self.assertFalse(self.ps1 == self.ps3)

    def testNe(self):
        self.assertNotEqual(self.ps1, self.ps2)
        self.assertTrue(self.ps2 != self.ps3)
        self.assertTrue(self.ps2 != self.ps4)
        self.assertFalse(self.ps1 != self.ps4)

    def testBuildFrom(self):
        D = self.ps1.buildFrom(Pitch('d'))
        self.assertTrue(Pitch('d') in D)
        self.assertTrue(Pitch('f', 2) in D)
        self.assertTrue(Pitch('a') in D)
        self.assertEqual(len(D), 3)
        Fis7 = self.ps2.buildFrom(Pitch('f', 2))
        self.assertTrue(Pitch('f', 2) in Fis7)
        self.assertTrue(Pitch('a', 2) in Fis7)
        self.assertTrue(Pitch('c', 2, 2) in Fis7)
        self.assertTrue(Pitch('e', 0, 2) in Fis7)
        self.assertEqual(len(Fis7), 4)

