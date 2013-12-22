#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering
#from opeNotes.pitch import Pitch, Octave


intervalTypes = ['dim', 'minor', 'perfect', 'major', 'aug']


class Interval(object):

    __slots__ = ['octaves', 'number', 'type_', 'dimAugFolds']

    def __init__(self, number, type_=None, dimAugFolds=None):
        self.octaves = (number - 1) // 7
        self.number = (number - 1) % 7 + 1
        if type_ is None:
            dimAugFolds = 0
            type_ = 'perfect' if self.number in [1, 4, 5] else 'major'
        if dimAugFolds is None:
            dimAugFolds = 0 if type_ in intervalTypes[1:4] else 1
        self.dimAugFolds = dimAugFolds
        self.type_ = type_

    @staticmethod
    def fromPitches(pitch1, pitch2):
        return None

    def __str__(self):
        result = str(self.number + self.octaves * 7)
        if self.number in [1, 4, 5]:
            return result + ''.join(['>' if self.type_ == 'dim' else
                                     '<' for _ in range(self.dimAugFolds)])
        if self.number in [2, 3, 6]:
            if self.type_ == 'minor':
                return result + '>'
            if self.type_ == 'dim':
                return result + \
                    ''.join(['>' for _ in range(self.dimAugFolds + 1)])
            if self.type_ == 'aug':
                return result + ''.join(['<' for _ in range(self.dimAugFolds)])
        if self.number == 7:
            if self.type_ == 'major':
                return result + '<'
            if self.type_ == 'aug':
                return result + \
                    ''.join(['<' for _ in range(self.dimAugFolds + 1)])
            if self.type_ == 'dim':
                return result + ''.join(['>' for _ in range(self.dimAugFolds)])
        return result

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.octaves, self.number, self.type_, self.dimAugFolds) == \
            (other.octaves, other.number, other.type_, other.dimAugFolds)

    def __ne__(self, other):
        return not self.__eq__(other)

