from Enitites import Ore

class ResultCalculator:
    def ResolveOreUnitValue(self, oreCount, totalValue):
        return totalValue / oreCount

    def CalculateOreUnitsValue(self, oreCount, ore):
        return oreCount * ore.Value