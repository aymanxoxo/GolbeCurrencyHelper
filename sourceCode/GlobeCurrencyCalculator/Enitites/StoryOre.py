from GlobeCurrencyCalculator.Enitites import Story, Ore

class StoryOre(Story, Ore):
    def SetParts(self, leftPart, rightPart):
        self.LeftPart = leftPart
        self.RightPart = rightPart