from GlobeCurrencyCalculator.Enitites import Story, Roman

class StoryRoman(Story, Roman):
    def SetParts(self, leftPart, rightPart):
        self.LeftPart = leftPart
        self.RightPart = rightPart