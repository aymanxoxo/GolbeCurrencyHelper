from GlobeCurrencyCalculator.HelperModule import List
from GlobeCurrencyCalculator.Enitites import Ore

class OreProvider:
    def __init__(self):
        self.__ores = List()
        
    def Add(self, ore):
        self.__ores.append(ore)

    def Get(self, oreName):
        return self.__ores.FirstOrDefault(self.__filter, oreName)

    def __filter(self, ore, compareVal):
        if ore.Name.upper() == compareVal.upper():
            return True
        else:
            return False