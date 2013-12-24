#!/usr/bin/python
# -*- coding: utf-8 -*-


from copy import copy
from functools import total_ordering
from opeNotes.interval import Interval


class Chord(object):

    __slots__ = ['intervals']

    def __init__(self, *intervals):
        self.intervals = list(intervals)

    def buildFrom(self, pitch):
        tmp = copy(pitch)
        result = [tmp]
        for interval in self.intervals:
            tmp += interval
            result.append(tmp)
        return result

    def __str__(self):
        return str(self.intervals)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if len(self.intervals) != len(other.intervals):
            return False
        for i in range(len(self.intervals)):
            if self.intervals[i] != other.intervals[i]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

