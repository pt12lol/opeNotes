#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering


@total_ordering
class RhythmicValue(object):
    """Represents class of music rhythmic values.

    Attrs:
        value (int): describing part of whole note (should be positive integer
            power of 2)
        dots  (int): describing extension of base rhythmic value (each dot
            extend half of last extension value)
    """

    __slots__ = ['value', 'dots']

    def __init__(self, value=None, dots=None):
        """Creates instance of RhythmicValue by value and number of dots.

        Args:
            value (int): part of whole note (should be positive integer
                power of 2) (default: 4)
            dots  (int): number of extending dots (should be positive integer
                value) (default: 0)
        """
        if value is None:
            value = 4
        if dots is None:
            dots = 0
        self.value = value
        self.dots = dots

    def __str__(self):
        """Returns string describing rhythmic value in LilyPond notation.

        Returns:
            string describing rhythmic value in LilyPond notation
        """
        return str(self.value) + ''.join(['.' for _ in range(self.dots)])

    def __repr__(self):
        """Returns string describing rhythmic value in LilyPond notation.

        Returns:
            string describing rhythmic value in LilyPond notation
        """
        return self.__str__()

    def __eq__(self, other):
        """Checks whether two rhythmic values are the same.

        Args:
            other (RhythmicValue): rhythmic value to compare with self
        Returns:
            result of equality of self pair of value and dots number with other
                pair of vaue and dots number
        """
        return (self.value, self.dots) == (other.value, other.dots)

    def __ne__(self, other):
        """Checks whether two rhythmic values aren't the same.

        Args:
            other (RhythmicValue): rhythmic value to compare with self
        Returns:
            result of non-equality of self pair of value and dots number with
                other pair of vaue and dots number
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compares two rhythmic values each other.

        Args:
            other (RhythmicValue): rhythmic value to compare with self
        Returns:
            result of comparison of length of last two rhythmic values
        """
        return self.value > other.value if self.value != other.value \
            else self.dots < other.dots

