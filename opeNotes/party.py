#!/usr/bin/python
# -*- coding: utf-8 -*-


class Party(object):

    __slots__ = ['notes']

    def __init__(self, *notes):
        self.notes = list(notes)

    def __repr__(self):
        return '{ ' + ' '.join([str(note) for note in self.notes]) + ' }'

    def __str__(self):
        return self.__repr__()

