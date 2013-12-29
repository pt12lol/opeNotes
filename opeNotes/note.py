#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering
from opeNotes.rhythmicValue import RhythmicValue


class Note(object):

    __slots__ = ['rhythmicValue', 'pitches']

    def __init__(self, value=None, dots=None, *pitches):
        if value is None:
            value = 4
        if dots is None:
            dots = 0
        self.rhythmicValue = RhythmicValue(value, dots)
        self.pitches = list(pitches)

    @staticmethod
    def fromRhythmValAndPitches(rhythmicValue=None, *pitches):
        if rhythmicValue is None:
            rhythmicValue = RhythmicValue()
        return Note(rhythmicValue.value, rhythmicValue.dots, *pitches)

    @staticmethod
    def fromRhythmValAndStruct(rhythmicValue=None,
                               startPitch=None, chord=None):
        if rhythmicValue is None:
            rhythmicValue = RhythmicValue()
        return Note(rhythmicValue.value, rhythmicValue.dots,
                    *(chord.buildFrom(startPitch)))

    def __repr__(self):
        return (('<' + ' '.join([str(pitch) for pitch in self.pitches]) + '>')
                if len(self.pitches) > 0 else 'r') + str(self.rhythmicValue)

    def __str__(self):
        return self.__repr__()

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

