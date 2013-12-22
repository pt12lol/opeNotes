#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering
from opeNotes.rhythmicValue import RhythmicValue
from opeNotes.pitch import Pitch, Octave


class Note(object):

    __slots__ = ['rhythmicValue', 'pitches']

    def __init__(self, value=None, dots=None, *pitches):
        if value is None:
            value = 4
        if dots is None:
            dots = 0
        if len(pitches) == 0:
            pitches = Pitch(),
        self.rhythmicValue = RhythmicValue(value, dots)
        self.pitches = list(pitches)

    @staticmethod
    def fromRhythmicValue(rhythmicValue=None, *pitches):
        if rhythmicValue is None:
            rhythmicValue = RhythmicValue()
        return Note(rhythmicValue.value, rhythmicValue.dots, *pitches)

    def __str__(self):
        return '<' + ' '.join([str(pitch) for pitch in self.pitches]) + '>' \
            + str(self.rhythmicValue)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.rhythmicValue != other.rhythmicValue:
            return False
        for selfPitch in self.pitches:
            broken = False
            for otherPitch in other.pitches:
                if selfPitch.eqNames(otherPitch):
                    broken = True
                    break
            if not broken:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

