#!/usr/bin/python
# -*- coding: utf-8 -*-


<<<<<<< HEAD
=======
from functools import total_ordering
from opeNotes.rhythmicValue import RhythmicValue
from opeNotes.pitch import Pitch, Octave


>>>>>>> ed3bea2bba80c9396d9a0cc8e9adae0cabc693b6
class Party(object):

    __slots__ = ['notes']

    def __init__(self, *notes):
        self.notes = list(notes)

    def __str__(self):
        return '{ ' + ' '.join([str(note) for note in self.notes]) + ' }'

    def __repr__(self):
        return self.__str__()

