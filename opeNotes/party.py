#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering
from opeNotes.rhythmicValue import RhythmicValue
from opeNotes.pitch import Pitch, Octave


class Party(object):

    __slots__ = ['notes']

    def __init__(self, *notes):
        self.notes = list(notes)

    def __str__(self):
        return '{ ' + ' '.join([str(note) for note in self.notes]) + ' }'

    def __repr__(self):
        return self.__str__()

