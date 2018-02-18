from GlobeCurrencyCalculator.Enitites import Roman

class RomanSynonym(Roman):
    def __init__(self, synonum, roman = None):
        self.Synonum = synonum
        super(RomanSynonym, self).__init__(roman.RomanNumber, roman.Value)