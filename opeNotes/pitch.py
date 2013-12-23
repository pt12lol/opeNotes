#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering
from opeNotes.octave import Octave
from opeNotes.interval import Interval, scaleRels


pitchNames = ['c', 'd', 'e', 'f', 'g', 'a', 'b']


@total_ordering
class Pitch(object):

    __slots__ = ['name', 'alteration', 'octave']

    def __init__(self, name=None, alteration=None,
                 octaveLines=None, octaveSize=None):
        if name is None:
            name = 'a'
        if alteration is None:
            alteration = 0
        if octaveLines is None:
            octaveLines = 1
        if octaveSize is None:
            octaveSize = 'lower'
        self.name = name
        self.alteration = alteration
        self.octave = Octave(octaveLines, octaveSize)

    @staticmethod
    def fromOctave(name=None, alteration=None, octave=None):
        if name is None:
            name = 'a'
        if alteration is None:
            alteration = 0
        if octave is None:
            octave = Octave()
        return Pitch(name, alteration, octave.lines, octave.size)

    def quartertonesFromC(self):
        return scaleRels[pitchNames.index(self.name)] * 2 + self.alteration

    def cmpPitch(self, other):
        if self < other:
            return -1
        if self > other:
            return 1
        return 0

    def eqNames(self, other):
        return (self.name, self.alteration, self.octave) == \
            (other.name, other.alteration, other.octave)

    def __repr__(self):
        result = self.name
        if self.alteration == 0:
            return result + str(self.octave)
        elif self.alteration == 1:
            result += 'ih'
        elif self.alteration == 2:
            result += 'is'
        elif self.alteration == 3:
            result += 'isih'
        elif self.alteration == 4:
            result += 'isis'
        elif self.alteration == -1:
            result += 'eh'
        elif self.alteration == -2:
            result += 'es'
        elif self.alteration == -3:
            result += 'eseh'
        elif self.alteration == -4:
            result += 'eses'
        return result + str(self.octave)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        selfQuartertones = self.quartertonesFromC()
        otherQuartertones = other.quartertonesFromC()
        selfAddOctaves = selfQuartertones // 24
        otherAddOctaves = otherQuartertones // 24
        selfQuartertones %= 24
        otherQuartertones %= 24
        octaves = self.octave + selfAddOctaves - other.octave - otherAddOctaves
        quartertones = selfQuartertones - otherQuartertones
        return quartertones + (octaves * 24) == 0

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        selfQuartertones = self.quartertonesFromC()
        otherQuartertones = other.quartertonesFromC()
        selfAddOctaves = selfQuartertones // 24
        otherAddOctaves = otherQuartertones // 24
        selfQuartertones %= 24
        otherQuartertones %= 24
        octaves = self.octave + selfAddOctaves - other.octave - otherAddOctaves
        quartertones = selfQuartertones - otherQuartertones
        return quartertones + (octaves * 24) < 0

