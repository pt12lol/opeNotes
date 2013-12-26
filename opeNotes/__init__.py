from opeNotes.octave import Octave, octaveSizes
from opeNotes.pitch import Pitch, pitchNames, semitones
from opeNotes.rhythmicValue import RhythmicValue
from opeNotes.note import Note
from opeNotes.interval import Interval, intervalTypes, scaleRels
from opeNotes.pitchesStructure import PitchesStructure
from opeNotes.party import Party

lyTemplate = r"""\version "2.16.2"
\score
{
    \new Staff << %s >>
    %s
}
"""

lyPdfTemplate = lyTemplate % ('%s', '')
lyMidiTemplate = lyTemplate % ('%s', r'\midi { \context { \Staff } }')

