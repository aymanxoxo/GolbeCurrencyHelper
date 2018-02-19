from WorkflowModule import Workflow
import PersistentModule
from Enitites import Ore
from CalculationModule import ResultCalculator, RomanCalculator

class StoryOreWf(Workflow):

    def Handle(self):
        romanNumericProvider = PersistentModule.RomanNumericProvider()
        resultCalc = ResultCalculator()
        romanCalc = RomanCalculator()
        oreProvider = PersistentModule.OreProvider()

        if self.InputEntity == None or self.InputEntity.LeftPart == None or self.InputEntity.RightPart == None:
            raise ValueError

        oreInSynonumUnits = self.InputEntity.LeftPart.strip().upper()
        valueInCredits = self.InputEntity.RightPart.strip().upper()

        totalValue = valueInCredits.lower().replace('credits', '')
        totalValue = int(totalValue)

        oreAndSyns = self.ExtractOreAndSynonums(oreInSynonumUnits)
        oreName = oreAndSyns[0]

        unitsCountInRomanNumber = oreAndSyns[1]

        oreUnits = romanCalc.CalculatorRomanValue(unitsCountInRomanNumber)

        oreUnitValue = resultCalc.ResolveOreUnitValue(oreUnits, totalValue)

        oreProvider.Add(Ore(oreName, oreUnitValue))
        
        return '\n info recorded'