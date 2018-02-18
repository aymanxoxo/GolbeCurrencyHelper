from GlobeCurrencyCalculator.WorkflowModule import IWorkflow
from GlobeCurrencyCalculator.AnalysisModule import Analysis
from GlobeCurrencyCalculator.PersistentModule import OreProvider, RomanNumericProvider
from GlobeCurrencyCalculator.Enitites import Ore
from GlobeCurrencyCalculator.CalculationModule import ResultCalculator

class StoryOreWf(IWorkflow):

    def Handle(self):
        analysis = Analysis()
        romanNumericProvider = RomanNumericProvider()
        romanCalc = ResultCalculator()
        oreProvider = OreProvider()

        if self.InputEntity == None or self.InputEntity.LeftPart == None or self.InputEntity.RightPart == None:
            raise ValueError

        oreInSynonumUnits = self.InputEntity.LeftPart.strip().upper()
        valueInCredits = self.InputEntity.RightPart.strip().upper()

        totalValue = valueInCredits.lower().replace('credits', '')
        totalValue = int(totalValue)

        oreName = oreInSynonumUnits.split('')
        oreName = oreName[len(oreName) - 1: 1].strip()

        synonumsStr = oreInSynonumUnits.replace(oreName, '').split(' ')
        unitsCountInRomanNumber = ""

        for synonumStr in synonumsStr:
            s = analysis.GetRomanSynonum(synonumStr)
            if s != None:
                unitsCountInRomanNumber += s.RomanNumber

        oreUnits = romanNumericProvider.GetNumericValue(unitsCountInRomanNumber)

        oreUnitValue = romanCalc.ResolveOreUnitValue(oreUnits, oreName, totalValue)

        oreProvider.Add(Ore(oreName, oreUnitValue))
        
        return '\n info recorded'