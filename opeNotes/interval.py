#!/usr/bin/python
# -*- coding: utf-8 -*-


intervalTypes = ['dim', 'minor', 'perfect', 'major', 'aug']
intervalDirections = ['up', 'down']
scaleRels = [0, 2, 4, 5, 7, 9, 11]


class Interval(object):

    __slots__ = ['octaves', 'number', 'direction', 'type_', 'dimAugFolds']

    def __init__(self, number, direction=None, type_=None, dimAugFolds=None):
        self.octaves = (number - 1) // 7
        self.number = (number - 1) % 7 + 1
        if type_ is None:
            dimAugFolds = 0
            type_ = 'perfect' if self.number in [1, 4, 5] else 'major'
        if dimAugFolds is None:
            dimAugFolds = 0 if type_ in intervalTypes[1:4] else 1
        self.dimAugFolds = dimAugFolds
        if direction is None:
            direction = 'up'
        self.direction = direction
        self.type_ = type_

    def semitones(self):
        result = scaleRels[self.number - 1] + self.octaves * 12
        if self.type_ == 'aug':
            return result + self.dimAugFolds
        if self.type_ == 'minor':
            return result - 1
        if self.type_ == 'dim':
            return result - self.dimAugFolds - 1
        return result

    def __str__(self):
        dim, aug = '>', '<'
        result = str(self.number + self.octaves * 7)
        if self.number in [1, 4, 5]:
            return result + ''.join([dim if self.type_ == 'dim' else
                                     aug for _ in range(self.dimAugFolds)])
        if self.number in [2, 3, 6]:
            if self.type_ == 'minor':
                return result + '>'
            if self.type_ == 'dim':
                return result + \
                    ''.join([dim for _ in range(self.dimAugFolds + 1)])
            if self.type_ == 'aug':
                return result + ''.join([aug for _ in range(self.dimAugFolds)])
        if self.number == 7:
            if self.type_ == 'major':
                return result + aug
            if self.type_ == 'aug':
                return result + \
                    ''.join([dim for _ in range(self.dimAugFolds + 1)])
            if self.type_ == 'dim':
                return result + ''.join([dim for _ in range(self.dimAugFolds)])
        return result

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.octaves, self.number, self.direction, self.type_,
                self.dimAugFolds) == (other.octaves, other.number,
                                      other.direction, other.type_,
                                      other.dimAugFolds)

    def __ne__(self, other):
        return not self.__eq__(other)

