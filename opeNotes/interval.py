#!/usr/bin/python
# -*- coding: utf-8 -*-


intervalTypes = ['dim', 'minor', 'perfect', 'major', 'aug']
scaleRels = [0, 2, 4, 5, 7, 9, 11]


class Interval(object):

    __slots__ = ['octaves', 'number', 'type_', 'direction', 'dimAugFolds']

    def __init__(self, number, type_=None, dimAugFolds=None):
        self.direction = (1 if number > 0 else -1)
        self.number = (((number - self.direction) * self.direction) % 7) + 1
        self.octaves = (number * self.direction - 1) // 7
        if type_ is None:
            type_ = 'perfect' if self.number in [1, 4, 5] else 'major'
        if dimAugFolds is None:
            dimAugFolds = 0 if type_ in intervalTypes[1:4] else 1
        self.dimAugFolds = dimAugFolds
        self.type_ = type_

    def semitones(self):
        result = scaleRels[self.number - 1] + self.octaves * 12
        if self.type_ == 'aug':
            result += self.dimAugFolds
        elif self.type_ == 'minor':
            result -= 1
        elif self.type_ == 'dim':
            result -= self.dimAugFolds - 1
        return result * self.direction

    def __repr__(self):
        dim, aug = '>', '<'
        result = str((self.number + self.octaves * 7) * self.direction)
        if self.number in [1, 4, 5]:
            return result + ''.join([dim if self.type_ == 'dim' else
                                     aug for _ in range(self.dimAugFolds)])
        if self.number in [2, 3, 6]:
            if self.type_ == 'minor':
                return result + dim
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

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return (self.octaves, self.number, self.direction, self.type_,
                self.dimAugFolds) == (other.octaves, other.number,
                                      other.direction, other.type_,
                                      other.dimAugFolds)

    def __ne__(self, other):
        return not self.__eq__(other)

