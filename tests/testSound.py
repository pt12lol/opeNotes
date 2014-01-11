#!/usr/bin/pythpn
# -*- cpding: utf-8 -*-


import unittest
from opeNotes.interval import Interval
from opeNotes.sound import Sound


class TestSound(unittest.TestCase):

    def setUp(self):
        self.s1 = Sound()
        self.s2 = Sound('a', 0)
        self.s3 = Sound('c', -3)
        self.s4 = Sound('b', 4)
        self.s5 = Sound('a', 0)
        self.s6 = Sound('c', 1)
        self.s7 = Sound('c', 2)

    def testRepr(self):
        self.assertEqual(str(self.s1), "a")
        self.assertEqual(str(self.s2), "a")
        self.assertEqual(str(self.s3), "ceseh")
        self.assertEqual(str(self.s4), "bisis")
        self.assertEqual(str(self.s5), "a")
        self.assertEqual(str(self.s6), "cih")
        self.assertEqual(str(self.s7), "cis")

    def testEq(self):
        self.assertEqual(self.s1, self.s5)
        self.assertEqual(self.s4, self.s7)
        self.assertTrue(self.s1 == self.s5)
        self.assertTrue(self.s7 == self.s4)
        self.assertFalse(self.s2 == self.s4)
        self.assertFalse(self.s3 == self.s4)
        self.assertFalse(self.s3 == self.s5)

    def testNe(self):
        self.assertNotEqual(self.s1, self.s3)
        self.assertTrue(self.s2 != self.s3)
        self.assertTrue(self.s2 != self.s4)
        self.assertFalse(self.s1 != self.s5)
        self.assertFalse(self.s4 != self.s7)

    def testAdd(self):
        tmp = self.s2
        tmp += Interval(3)
        self.assertTrue(tmp.eqNames(Sound('c', 2)))
        self.assertTrue((tmp + Interval(2, 'minor')).eqNames(Sound('d')))
        self.assertTrue((tmp + Interval(4)).eqNames(Sound('f', 2)))
        self.assertTrue((tmp + Interval(-5, 'aug')).eqNames(Sound('f', 0)))
        self.assertTrue((tmp + Interval(-2)).eqNames(Sound('b', 0)))

    def testSub(self):
        tmp = self.s2
        tmp -= Interval(-6, 'minor')
        self.assertTrue(tmp.eqNames(Sound('f')))
        self.assertTrue((tmp - Interval(-2, 'minor')).eqNames(Sound('g', -2)))
        self.assertTrue((tmp - Interval(-5, 'aug')).eqNames(Sound('c', 2)))
        self.assertTrue((tmp - Interval(10)).eqNames(Sound('d', -2)))
        self.assertTrue((tmp - Interval(2)).eqNames(Sound('e', -2)))

