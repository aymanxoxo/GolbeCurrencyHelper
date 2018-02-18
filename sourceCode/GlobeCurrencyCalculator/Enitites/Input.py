from GlobeCurrencyCalculator.WorkflowModule import Workflow

class Input:
    def __init__(self, sentence, type):
        self.Sentence = sentence
        self.Type = type
        self.Workflow = self.GetWorkflow()

    def SetParts(self, leftPart, rightPart):
        pass

    def GetWorkflow(self):
        pass