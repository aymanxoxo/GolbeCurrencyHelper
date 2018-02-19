from Enitites import Story, Roman
from WorkflowModule import StoryRomanWf

class StoryRoman(Story, Roman):
    def SetParts(self, leftPart, rightPart):
        self.LeftPart = leftPart
        self.RightPart = rightPart
        self.GetWorkflow = self.GetWorkflow(this)
    
    def GetWorkflow(self):
        q = StoryRomanWf(self)
        return q