from GlobeCurrencyCalculator.WorkflowModule import Workflow
from GlobeCurrencyCalculator.PersistentModule import OreProvider, RomanNumericProvider
from GlobeCurrencyCalculator.Enitites import Ore
from GlobeCurrencyCalculator.CalculationModule import ResultCalculator, RomanCalculator

class StoryOreWf(Workflow):

    def Handle(self):
        romanNumericProvider = RomanNumericProvider()
        resultCalc = ResultCalculator()
        romanCalc = RomanCalculator()
        oreProvider = OreProvider()

        if self.InputEntity == None or self.InputEntity.LeftPart == None or self.InputEntity.RightPart == None:
            raise ValueError

        oreInSynonumUnits = self.InputEntity.LeftPart.strip().upper()
        valueInCredits = self.InputEntity.RightPart.strip().upper()

        totalValue = valueInCredits.lower().replace('credits', '')
        totalValue = int(totalValue)

        oreName = oreInSynonumUnits.split(' ')
        oreName = oreName[len(oreName) - 1: 1].strip()

        synonumsStr = oreInSynonumUnits.replace(oreName, '').split(' ')
        unitsCountInRomanNumber = self.convertSynonumsToRomans(synonumsStr)

        oreUnits = romanCalc.CalculatorRomanValue(unitsCountInRomanNumber)

        oreUnitValue = resultCalc.ResolveOreUnitValue(oreUnits, oreName, totalValue)

        oreProvider.Add(Ore(oreName, oreUnitValue))
        
        return '\n info recorded'