#!/usr/bin/python
# -*- coding: utf-8 -*-

from opeNotes import Octave, Pitch, Interval, PitchesStructure, Note, Party
from opeNotes import lyMidiTemplate
from random import randint

scale = PitchesStructure(Interval(2), Interval(2), Interval(2, 'minor'),
    Interval(2), Interval(2), Interval(2), Interval(2, 'minor'))
pitches = scale.buildFrom(Pitch('c'))

def main():
    current = 0
    party = Party()
    party.notes.append(Note(32, 0, Pitch('d')))
    for i in range(256):
        if randint(0, 1):
            interval = scale.intervals[current % 7]
            current += 1
        else:
            interval = -(scale.intervals[(current - 1) % 7])
            current -= 1
        lastPitch = party.notes[-1].pitches[0]
        party.notes.append(Note(32, 0, lastPitch + interval))
    print(lyMidiTemplate % str(party))

if __name__ == '__main__':
    main()

