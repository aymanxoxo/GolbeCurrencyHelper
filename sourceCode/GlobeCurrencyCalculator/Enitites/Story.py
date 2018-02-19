from Enitites import Input

class Story(Input):
    def __init__(self, leftPart, rightPart):
        self.LeftPart = leftPart
        self.RightPart = rightPart
        self.Workflow = self.GetWorkflow()