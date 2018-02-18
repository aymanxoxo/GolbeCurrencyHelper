from GlobeCurrencyCalculator.WorkflowModule import Workflow
from GlobeCurrencyCalculator.CalculationModule import RomanCalculator

class QuestionRomanWf(Workflow):

    def Handle(self):
        romanCal = RomanCalculator()

        question = self.InputEntity.QuestionPhrase
        romanStr = self.convertSynonumsToRomans(question)
        result = romanCal.CalculatorRomanValue(romanStr)

        return "\n " + question + " is " + str(result)


