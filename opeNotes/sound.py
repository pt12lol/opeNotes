#!/usr/bin/python
# -*- coding: utf-8 -*-


from opeNotes.interval import Interval, semitones


pitchNames = ['c', 'd', 'e', 'f', 'g', 'a', 'b']


class Sound(object):

    __slots__ = ['name', 'alteration']

    def __init__(self, name=None, alteration=None):
        if name is None:
            name = 'a'
        if alteration is None:
            alteration = 0
        self.name = name
        self.alteration = alteration

    def quartertonesFromC(self):
        return sum(semitones[:pitchNames.index(self.name)])*2 + self.alteration

    def eqNames(self, other):
        return (self.name, self.alteration) == (other.name, other.alteration)

    def __repr__(self):
        result = self.name
        if self.alteration == 0:
            return result
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
        return result

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.quartertonesFromC() % 24 == other.quartertonesFromC() % 24

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        index = (pitchNames.index(self.name)
                 + (other.number - 1) * other.direction) % 7
        result = Sound(pitchNames[index], self.alteration)
        difference = 0
        while index != pitchNames.index(self.name):
            index = (index - other.direction) % 7
            difference += semitones[index if other.direction > 0
                                    else ((index - 1) % 7)]
        difference *= other.direction
        result.alteration += ((other.semitones() - difference) * 2)
        if result.alteration <= -24:
            result.alteration += 24
        elif result.alteration >= 24:
            result -= 24
        return result

    def __sub__(self, other):
        return self + Interval(-other.direction * other.number,
                               other.type_, other.dimAugFolds)

