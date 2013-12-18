#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering


@total_ordering
class RhythmicValue(object):

    __slots__ = ['value', 'dots']

    def __init__(self, value=None, dots=None):
        if value is None:
            value = 4
        if dots is None:
            dots = 0
        self.value = value
        self.dots = dots

    def __str__(self):
        return str(self.value) + ''.join(['.' for _ in range(self.dots)])

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.value, self.dots) == (other.value, other.dots)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.value > other.value if self.value != other.value \
            else self.dots < other.dots

