from helpers import findex, flip
scale = [
    ["a"],
    ["a#", "bb"],
    ["b", "cb"],
    ["c", "b#"],
    ["c#", "db"],
    ["d"],
    ["d#", "eb"],
    ["e", "fb"],
    ["f", "e#"],
    ["f#", "gb"],
    ["g"],
    ["g#", "ab"]
]

# immutable by nature
class Note:
    def __init__(self, note):
        self.note = None;
        self.identity = None;
        
        for note_identity in scale:
            if note in note_identity:
                self.note = note
                self.identity = note_identity
        if not self.note:
            raise Exception("Not valid note")
    # alternate identity
    def alt(self):
        return self.identity[findex(flip(self.identity.index(self.note)), self.identity)]
    # up by x semitones
    def up(self, x=1):
        return Note(scale[findex(scale.index(self.identity)+x, scale)][0])
