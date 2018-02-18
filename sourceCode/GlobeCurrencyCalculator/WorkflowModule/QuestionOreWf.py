from GlobeCurrencyCalculator.WorkflowModule import Workflow
from GlobeCurrencyCalculator.PersistentModule import OreProvider
from GlobeCurrencyCalculator.CalculationModule import RomanCalculator

class QuestionOreWf(Workflow):
    
    def Handle(self):
        oreProvider = OreProvider()
        romanCalc = RomanCalculator()
        
        question = self.InputEntity.QuestionPhrase

        oreAndRoman = self.ExtractOreAndSynonums(question)

        oreName = oreAndRoman[0]
        romanNumber = oreAndRoman[1]

        ore = oreProvider.Get(oreName)
        unitsCount = romanCalc.CalculatorRomanValue(romanNumber)

        return '\n ' + question + ' is ' + unitsCount * ore.Value + ' credits'


