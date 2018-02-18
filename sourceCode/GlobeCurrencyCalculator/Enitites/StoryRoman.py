from GlobeCurrencyCalculator.Enitites import Story, Roman
from GlobeCurrencyCalculator.WorkflowModule import StoryRomanWf

class StoryRoman(Story, Roman):
    def SetParts(self, leftPart, rightPart):
        self.LeftPart = leftPart
        self.RightPart = rightPart
    
    def GetWorkflow(self):
        q = StoryRomanWf(self)
        return q