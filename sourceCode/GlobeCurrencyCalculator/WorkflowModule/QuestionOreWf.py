from WorkflowModule import Workflow
import PersistentModule
from CalculationModule import RomanCalculator

class QuestionOreWf(Workflow):
    
    def Handle(self):
        oreProvider = PersistentModule.OreProvider()
        romanCalc = RomanCalculator()
        
        question = self.InputEntity.QuestionPhrase

        oreAndRoman = self.ExtractOreAndSynonums(question)

        oreName = oreAndRoman[0]
        romanNumber = oreAndRoman[1]

        ore = oreProvider.Get(oreName)
        unitsCount = romanCalc.CalculatorRomanValue(romanNumber)

        return '\n ' + question + ' is ' + str(unitsCount * ore.Value) + ' credits'


