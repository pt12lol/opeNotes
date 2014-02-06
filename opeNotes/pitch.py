#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import total_ordering
from opeNotes.sound import Sound, pitchNames
from opeNotes.octave import Octave
from opeNotes.interval import Interval, semitones


@total_ordering
class Pitch(object):
    """Represents class of music pitches.

    Attrs:
        sound  (Sound):  describing name and alteration of pitch
        octave (Octave): describing octave of pitch
    """

    __slots__ = ['sound', 'octave']

    def __init__(self, name=None, alteration=None,
                 octaveLines=None, octaveSize=None):
        """Creates instance of Pitch by name, alteration and octave parameters

        Args:
            name        (str): name of pitch; should be one-letter string from
                the pitchNames list (default: 'a')
            alteration  (int): alteration of pitch; should be integer value
                from -4 to 4 range (default: 0)
            octaveLines (int): lines of pitch's octave (default: 1)
            octaveSize  (str): case of letter in music notation of pitch's
                octave; should be only from set of opeNotes.octave.octaveSizes
                list - 'upper' or 'lower' (default: 'lower')
        """
        if name is None:
            name = 'a'
        if alteration is None:
            alteration = 0
        if octaveLines is None:
            octaveLines = 1
        if octaveSize is None:
            octaveSize = 'lower'
        self.sound = Sound(name, alteration)
        self.octave = Octave(octaveLines, octaveSize)

    @staticmethod
    def fromOctave(name=None, alteration=None, octave=None):
        """Static factory to product pitch from Octave.

        Args:
            name       (str):    name of pitch; should be one-letter string
                from the pitchNames list (default: 'a')
            alteration (int):    alteration of pitch; should be integer value
                from -4 to 4 range (default: 0)
            octave     (Octave): octave for pitch (default: Octave())
        """
        if name is None:
            name = 'a'
        if alteration is None:
            alteration = 0
        if octave is None:
            octave = Octave()
        return Pitch(name, alteration, octave.lines, octave.size)

    @staticmethod
    def fromSoundAndOctave(sound=None, octave=None):
        """Static factory to product pitch from Sound and Octave.

        Args:
            sound  (Sound):  sound of pitch (default: Sound())
            octave (Octave): octave for pitch (default: Octave())
        """
        if sound is None:
            sound = Sound()
        if octave is None:
            octave = Octave()
        return Pitch(sound.name, sound.alteration, octave.lines, octave.size)

    def cmpPitch(self, other):
        """Compares two pitches by their height.

        Args:
            other (Pitch): the other pitch to compare.
        Returns:
            -1 if self is lower, 1 if self is higher and 0 if both are the same
                height
        """
        if self < other:
            return -1
        if self > other:
            return 1
        return 0

    def eqNames(self, other):
        """Checks if names, alterations and octaves two pitches equal.

        Args:
            other (Pitch): the other pitch to compare
        Returns:
            equalation of tuples of self name, self alteration and self octave
                with other name, other alteration and other octave
        """
        return (self.sound.name, self.sound.alteration, self.octave) == \
            (other.sound.name, other.sound.alteration, other.octave)

    def __repr__(self):
        """Returns string describing pitch in LilyPond notation.

        Returns:
            string describing pitch in LilyPond notation
        """
        return str(self.sound) + str(self.octave)

    def __str__(self):
        """Returns string describing pitch in LilyPond notation.

        Returns:
            string describing pitch in LilyPond notation
        """
        return self.__repr__()

    def __eq__(self, other):
        """Checks equality of height of two pitches.

        Args:
            other (Pitch): the other pitch to compare
        Returns:
            result of equality of heights of two pitches
        """
        selfQuartertones = self.sound.quartertonesFromC()
        otherQuartertones = other.sound.quartertonesFromC()
        selfAddOctaves = selfQuartertones // 24
        otherAddOctaves = otherQuartertones // 24
        selfQuartertones %= 24
        otherQuartertones %= 24
        octaves = self.octave + selfAddOctaves - other.octave - otherAddOctaves
        quartertones = selfQuartertones - otherQuartertones
        return quartertones + (octaves * 24) == 0

    def __ne__(self, other):
        """Checks non-equality of height of two pitches.

        Args:
            other (Pitch): the other pitch to compare
        Returns:
            result of non-equalityi of heights of two pitches
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compares height of two pitches.

        Args:
            other (Pitch): the other pitch to compare
        Returns:
            result of comparison heights of two pitches
        """
        selfQuartertones = self.sound.quartertonesFromC()
        otherQuartertones = other.sound.quartertonesFromC()
        selfAddOctaves = selfQuartertones // 24
        otherAddOctaves = otherQuartertones // 24
        selfQuartertones %= 24
        otherQuartertones %= 24
        octaves = self.octave + selfAddOctaves - other.octave - otherAddOctaves
        quartertones = selfQuartertones - otherQuartertones
        return quartertones + (octaves * 24) < 0

    def __add__(self, other):
        """Adds to self interval.

        Args:
            other (Interval): interval to add to self
        Returns:
            pitch which is self increased of other interval
        """
        index = pitchNames.index(self.sound.name)
        delta = (other.number - 1 + other.octaves * 7) * other.direction
        index += delta
        octave = self.octave + (index // 7)
        index %= 7
        result = Pitch(pitchNames[index], self.sound.alteration,
                       octave.lines, octave.size)
        difference = 0
        while index != pitchNames.index(self.sound.name):
            index = (index - other.direction) % 7
            difference += semitones[index if other.direction > 0
                                    else ((index - 1) % 7)]
        difference *= other.direction
        result.sound.alteration += ((other.semitones() - difference) * 2)
        if result.sound.alteration <= -24:
            result.sound.alteration += 24
        elif result.sound.alteration >= 24:
            result.sound.alteration -= 24
        return result

    def __sub__(self, other):
        """Substracts from self interval.

        Args:
            other (Interval): interval to substract from self
        Returns:
            pitch which is self decreased of other interval
        """
        return self + Interval(-other.direction
                               * (other.number + other.octaves * 7),
                               other.type_, other.dimAugFolds)

