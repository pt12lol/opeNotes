#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering


octaveSizes = ['upper', 'lower']


@total_ordering
class Octave(object):
    """Represents class of music octaves.

    Attrs:
        lines (int): describing lines of octave
        size  (str): describing case of letter in music notation of octave;
            should be only from set of octaveSizes list - 'upper' or 'lower'
    """

    __slots__ = ['lines', 'size']

    def __init__(self, lines=None, size=None):
        """Creates instance of Octave by lines and size.

        Args:
            lines (int): lines of octave (default: 1)
            size  (str): case of letter in music notation of octave;
                should be only from set of octaveSizes list - 'upper'
                or 'lower' (default: 'lower')
        """
        if lines is None:
            lines = 1
        if size is None:
            size = 'lower'
        self.lines = lines
        self.size = size

    def __repr__(self):
        """Returns string describing octave in LilyPond notation.

        Returns:
            string describing octave in LilyPond notation
        """
        return ''.join([',' if self.size == 'upper' else "'"
                        for i in range(self.lines + 1
                        if self.size == 'upper' else self.lines)])

    def __str__(self):
        """Returns string describing octave in LilyPond notation.

        Returns:
            string describing octave in LilyPond notation
        """
        return self.__repr__()

    def __eq__(self, other):
        """Checks whether two octaves are the same.

        Args:
            other (Octave): octave to compare with self
        Returns:
            result of equality of self pair of lines and size with other pair
                of lines and size
        """
        return (self.lines, self.size) == (other.lines, other.size)

    def __ne__(self, other):
        """Checks whether two octaves aren't the same.

        Args:
            other (Octave): octave to compare with self
        Returns:
            result of non-equality of self pair of lines and size with other
                pair of lines and size
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compares two octaves each other.

        Args:
            other (Octave): octave to compare with self
        Returns:
            result of comparison of height of two octaves
        """
        return octaveSizes.index(self.size) < octaveSizes.index(other.size) \
            if octaveSizes.index(self.size) != octaveSizes.index(other.size) \
            else (self.lines < other.lines if self.size == 'lower'
                  else self.lines > other.lines)

    def __add__(self, other):
        """Adds to self octave integer and returns octave greater than self of
            other-number of octaves.

        Args:
            other (int): number of octaves to increase of self
        Returns:
            Octave greater than self of other-number of octaves
        """
        if self.size == 'lower' and other >= 0:
            return Octave(self.lines + other, 'lower')
        if self.size == 'upper' and other <= 0:
            return Octave(self.lines - other, 'upper')
        if self.size == 'lower' and other < 0:
            if self.lines + other < 0:
                return Octave(-(self.lines + other) - 1, 'upper')
            return Octave(self.lines + other, 'lower')
        if self.lines - other < 0:
            return Octave(-self.lines + other - 1, 'lower')
        return Octave(self.lines - other, 'upper')

    def __sub__(self, other):
        """Adds to self octave integer and returns octave lesser than self of
            other-number of octaves.

        Args:
            other (int/Octave):
                if other's type is int:
                    number of octaves to decrease of self
                else if other's type is Octave:
                    octave to substract from self octave
        Returns:
            if other's type is int:
                Octave lesser than self of other-number of octaves
            else if other's type is Octave:
                integer difference between self and other
        """
        if type(other) == int:
            return self.__add__(-other)
        result = 0;
        if self < other:
            while self < other + result:
                result -= 1
        elif self > other:
            while self > other + result:
                result += 1
        return result

