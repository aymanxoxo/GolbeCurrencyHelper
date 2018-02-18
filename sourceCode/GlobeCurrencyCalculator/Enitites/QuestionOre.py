from GlobeCurrencyCalculator.Enitites import Question, Ore

class QuestionOre(Question, Ore):
    def SetParts(self, leftPart, rightPart):
        self.QuestionPhrase = rightPart