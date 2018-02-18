from GlobeCurrencyCalculator.HelperModule import List
from GlobeCurrencyCalculator.Enitites import Ore

class OreProvider:
    __ores = List()

    def __init__(self):
        pass
        
    def Add(self, ore):
        ore.Name = ore.Name.upper()
        self.__ores.append(ore)

    def Get(self, oreName):
        return self.__ores.FirstOrDefault(self.__filter, oreName.upper())

    def __filter(self, ore, compareVal):
        if ore.Name.upper() == compareVal.upper():
            return True
        else:
            return False