#!/usr/bin/python
# -*- coding: utf-8 -*-

from opeNotes import Octave, Pitch, Interval, PitchesStructure, Note, Party
from opeNotes import lyMidiSoloTemplate
from random import randint

numberOfNotes = 256
rhythmicValue = 32
basePitchName = 'd'

scale = PitchesStructure(Interval(2, 'minor'), Interval(2, 'aug'),
                         Interval(2, 'minor'), Interval(2, 'aug'),
                         Interval(2, 'minor'), Interval(2),
                         Interval(2, 'minor'))
pitches = scale.buildFrom(Pitch(basePitchName))

def main():
    currentIndex = 0
    party = Party()
    party.notes.append(Note(rhythmicValue, 0, Pitch(basePitchName)))
    currentPitch = party.notes[-1].pitches[0]

    for i in range(numberOfNotes):
        if randint(0, 4):
            if randint(0, 1):
                interval = scale.intervals[currentIndex % 7]
                currentIndex += 1
            else:
                interval = -(scale.intervals[(currentIndex - 1) % 7])
                currentIndex -= 1
            currentPitch += interval
            party.notes.append(Note(rhythmicValue, 0, currentPitch))
        else:
            party.notes.append(Note(rhythmicValue, 0))

    for i in range(numberOfNotes):
        if randint(0, 4):
            if randint(0, 1):
                interval = scale.intervals[currentIndex % 7]
                currentIndex += 1
            else:
                interval = -(scale.intervals[(currentIndex - 1) % 7])
                currentIndex -= 1
            currentPitch += interval
            party.notes.append(Note(rhythmicValue, 0, currentPitch))
            if currentPitch.sound.name == 'c':
                for j in range(2, 9):
                    party.notes[-1].pitches.append(currentPitch + Interval(j))
        else:
            party.notes.append(Note(rhythmicValue, 0))

    for i in range(numberOfNotes / 2):
        if randint(0, 4):
            if randint(0, 1):
                interval = scale.intervals[currentIndex % 7]
                currentIndex += 1
            else:
                interval = -(scale.intervals[(currentIndex - 1) % 7])
                currentIndex -= 1
            currentPitch += interval
            party.notes.append(Note(rhythmicValue, 0, currentPitch))
        else:
            party.notes.append(Note(rhythmicValue, 0))

    for i in range(numberOfNotes / 2):
        if randint(0, 1):
            interval = scale.intervals[currentIndex % 7]
            currentIndex += 1
        else:
            interval = -(scale.intervals[(currentIndex - 1) % 7])
            currentIndex -= 1
        currentPitch += interval
        party.notes.append(Note(rhythmicValue, 0, currentPitch))

    for i in range(numberOfNotes):
        # if randint(0, 4):
            if randint(0, 1):
                interval = scale.intervals[currentIndex % 7]
                currentIndex += 1
            else:
                interval = -(scale.intervals[(currentIndex - 1) % 7])
                currentIndex -= 1
            currentPitch += interval
            party.notes.append(Note(rhythmicValue, 0, currentPitch))
            if randint(0, numberOfNotes) < i:
                party.notes[-1].pitches.append(currentPitch - Interval(10))
            if randint(0, numberOfNotes) < i:
                party.notes[-1].pitches.append(currentPitch + Interval(4))
            if currentPitch.sound.name == 'c':
                for j in range(2, 9):
                    party.notes[-1].pitches.append(currentPitch + Interval(j))
        # else:
        #     party.notes.append(Note(rhythmicValue, 0))
    print(lyMidiSoloTemplate % str(party))

if __name__ == '__main__':
    main()

