from musiclib import Note
import sys

# semishift.py <note> <by>

args = sys.argv
args.pop(0)

note = Note(args[0])
shifted = note.shift(int(args[1]))
print(shifted.note)