from GlobeCurrencyCalculator.Enitites import Ore

class ResultCalculator:
    def ResolveOreUnitValue(self, oreCount, ore, totalValue):
        ore.Value = totalValue / oreCount
        return ore

    def CalculateOreUnitsValue(self, oreCount, ore):
        return oreCount * ore.Value