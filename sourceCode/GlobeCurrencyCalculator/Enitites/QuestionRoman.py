from GlobeCurrencyCalculator.Enitites import Question, Roman

class QuestionRoman(Question, Roman):
    def SetParts(self, leftPart, rightPart):
        self.QuestionPhrase = rightPart