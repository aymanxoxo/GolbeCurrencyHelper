from GlobeCurrencyCalculator.Enitites import InputType, Roman
from GlobeCurrencyCalculator.HelperModule import List


class RomanNumericProvider:
    
    def __init__(self):
        self.values = List()
        self.values.extend(
        [
            Roman('I', 1),
            Roman('V', 5),
            Roman('X', 10),
            Roman('L', 50),
            Roman('C', 100),
            Roman('D', 500),
            Roman('M', 1000)
        ])

    def GetNumericValue(self, roman):
        return self.values.FirstOrDefault(self.__filter, roman.RomanNumber)

    def __filter(self, roman, compareVal):
        if roman.RomanNumber == compareVal:
            return True
        else:
            return False