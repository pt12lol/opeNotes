#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from opeNotes.note import Note, Pitch
from opeNotes.rhythmicValue import RhythmicValue


class TestNote(unittest.TestCase):

    def setUp(self):
        self.n1 = Note()
        self.n2 = Note(8, 1, Pitch('c', 2, 2), Pitch('e'), Pitch())
        self.n3 = Note.fromRhythmicValue(RhythmicValue(8, 0), Pitch('d'))
        self.n4 = Note(4, 0, Pitch('a'))
        self.n5 = Note(8, 1)
        self.n5.pitches.append(Pitch('c', 2, 2))
        self.n5.pitches.append(Pitch('e'))

    def testRepr(self):
        self.assertEqual(str(self.n1), "<a'>4")
        self.assertEqual(str(self.n2), "<cis'' e' a'>8.")
        self.assertEqual(str(self.n3), "<d'>8")
        self.assertEqual(str(self.n4), "<a'>4")
        self.assertEqual(str(self.n5), "<a' cis'' e'>8.")

    def testEq(self):
        self.assertEqual(self.n1, self.n4)
        self.assertEqual(self.n2, self.n5)
        self.assertTrue(self.n4 == self.n1)
        self.assertTrue(self.n5 == self.n2)
        self.assertFalse(self.n2 == self.n4)
        self.assertFalse(self.n3 == self.n4)
        self.assertFalse(self.n3 == self.n5)

    def testNe(self):
        self.assertNotEqual(self.n1, self.n2)
        self.assertTrue(self.n2 != self.n3)
        self.assertTrue(self.n2 != self.n4)
        self.assertFalse(self.n2 != self.n5)
        self.assertFalse(self.n1 != self.n4)

