#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering


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

    def __repr__(self):
        return ''.join([',' if self.size == 'upper' else "'"
                        for i in range(self.lines + 1
                        if self.size == 'upper' else self.lines)])

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return (self.size, self.lines) == (other.size, other.lines)

    def __ne__(self, other):
        return not self.__eq__(other)

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
        return self.__add__(-num)

