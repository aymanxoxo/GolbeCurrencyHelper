from Enitites import Question, Ore
from WorkflowModule import QuestionOreWf

class QuestionOre(Question, Ore):
    def SetParts(self, leftPart, rightPart):
        self.QuestionPhrase = rightPart
    
    def GetWorkflow(self):
        q = QuestionOreWf(self)
        return q