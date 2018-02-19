from Enitites.Input import Input

class Question(Input):
    def __init__(self, questionPhrase):
        self.QuestionPhrase = questionPhrase
        self.Workflow = self.GetWorkflow()