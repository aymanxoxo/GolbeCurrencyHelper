from GlobeCurrencyCalculator.Enitites import Story, Ore
from GlobeCurrencyCalculator.WorkflowModule import StoryOreWf

class StoryOre(Story, Ore):
    def SetParts(self, leftPart, rightPart):
        self.LeftPart = leftPart
        self.RightPart = rightPart
    
    def GetWorkflow(self):
        q = StoryOreWf(self)
        return q