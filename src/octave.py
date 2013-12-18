#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering


sizes = ['upper', 'lower']


@total_ordering
class Octave(object):

    __slots__ = ['lines', 'size']

    def __init__(self, lines=None, size=None):
        if lines is None:
            lines = 1
        if size is None:
            size = 'lower'
        self.lines = lines
        self.size = size

    def __repr__(self):
        return ''.join([',' if self.size == 'upper' else "'"
                        for i in range(self.lines + 1
                        if self.size == 'upper' else self.lines)])

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return (self.lines, self.size) == (other.lines, other.size)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return sizes.index(self.size) < sizes.index(other.size) \
            if sizes.index(self.size) != sizes.index(other.size) \
            else (self.lines < other.lines if self.size == 'lower'
                  else self.lines > other.lines)

    def __add__(self, other):
        if self.size == 'lower' and other >= 0:
            return Octave(self.lines + other, 'lower')
        if self.size == 'upper' and other <= 0:
            return Octave(self.lines - other, 'upper')
        if self.size == 'lower' and other < 0:
            if self.lines + other < 0:
                return Octave(-(self.lines + other) - 1, 'upper')
            return Octave(self.lines + other, 'lower')
        if self.lines - other < 0:
            return Octave(-self.lines + other - 1, 'lower')
        return Octave(self.lines + other, 'upper')

    def __sub__(self, other):
        if type(other) == int:
            return self.__add__(-other)
        result = 0;
        if self < other:
            while self < other + result:
                result -= 1
        elif self > other:
            while self > other + result:
                result += 1
        return result

