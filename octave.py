#!/usr/bin/python
# -*- coding: utf-8 -*-


from copy import copy
from functools import total_ordering
import unittest


octaveSizes = ['upper', 'lower']


@total_ordering
class Octave:

    def __init__(self, size=None, lines=None):
        if size == None:
            size = 'lower'
        if lines == None:
            linse = 1
        self.size = size
        self.lines = lines
        self.__str = self.__repr__

    def __repr__(self):
        return ''.join([',' if self.size == 'upper' else "'"
                        for i in range(self.lines + 1
                        if self.size == 'upper' else self.lines)])

    def __eq__(self, other):
        return (self.size, self.lines) == (other.size, other.lines)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return octaveSizes.index(self.size) < octaveSizes.index(other.size) \
            if octaveSizes.index(self.size) != octaveSizes.index(other.size) \
            else (self.lines < other.lines if self.size == 'lower'
                  else self.lines > other.lines)

    def __add__(self, num):
        if self.size == 'lower' and num >= 0:
            return Octave('lower', self.lines + num)
        if self.size == 'upper' and num <= 0:
            return Octave('upper', self.lines - num)
        if self.size == 'lower' and num < 0:
            if self.lines + num < 0:
                return Octave('upper', -(self.lines + num) - 1)
            return Octave('lower', self.lines + num)
        if self.lines - num < 0:
            return Octave('lower', -(self.lines + num) - 1)
        return Octave('upper', self.lines + num)

    def __sub__(self, num):
        return self + (-num)



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

    def testGe(self):
        self.assertGreaterEqual(self.o1, self.o2)
        self.assertGreaterEqual(self.o1, self.o5)
        self.assertTrue(self.o2 >= self.o3)
        self.assertTrue(self.o3 >= self.o4)
        self.assertTrue(self.o1 >= self.o5)
        self.assertFalse(self.o4 >= self.o5)

    def testAdd(self):
        tmp = copy(self.o1)
        tmp += 1
        self.assertEqual(tmp, Octave('lower', 2))
        self.assertEqual(tmp + 2, Octave('lower', 4))
        self.assertEqual(tmp + (-3), Octave('upper', 0))
        self.assertEqual(tmp + (-2), Octave('lower', 0))
        self.assertEqual(tmp + (-4), Octave('upper', 1))

    def testSub(self):
        tmp = copy(self.o1)
        tmp -= -1
        self.assertEqual(tmp, Octave('lower', 2))
        self.assertEqual(tmp - (-2), Octave('lower', 4))
        self.assertEqual(tmp - 3, Octave('upper', 0))
        self.assertEqual(tmp - 2, Octave('lower', 0))
        self.assertEqual(tmp - 4, Octave('upper', 1))



if __name__ == '__main__':
    unittest.main()

