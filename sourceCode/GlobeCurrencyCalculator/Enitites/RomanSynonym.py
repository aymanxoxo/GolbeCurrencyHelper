from Enitites.Roman import Roman

class RomanSynonym(Roman):
    def __init__(self, synonum, roman = None):
        self.Synonum = synonum
        self.RomanNumber = roman.RomanNumber
        self.Value = roman.Value