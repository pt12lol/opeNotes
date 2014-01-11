from opeNotes.octave import Octave, octaveSizes
from opeNotes.pitch import Pitch, pitchNames
from opeNotes.rhythmicValue import RhythmicValue
from opeNotes.note import Note
from opeNotes.interval import Interval, intervalTypes
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

