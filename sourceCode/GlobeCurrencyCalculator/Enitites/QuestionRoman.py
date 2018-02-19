from Enitites import Question, Roman
from WorkflowModule import QuestionRomanWf

class QuestionRoman(Question, Roman):
    def SetParts(self, leftPart, rightPart):
        self.QuestionPhrase = rightPart
    
    def GetWorkflow(self):
        q = QuestionRomanWf(self)
        return q