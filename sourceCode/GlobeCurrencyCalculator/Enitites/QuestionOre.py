from GlobeCurrencyCalculator.Enitites import Question, Ore
from GlobeCurrencyCalculator.WorkflowModule import QuestionOreWf

class QuestionOre(Question, Ore):
    def SetParts(self, leftPart, rightPart):
        self.QuestionPhrase = rightPart
    
    def GetWorkflow(self):
        q = QuestionOreWf(self)
        return q