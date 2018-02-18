from GlobeCurrencyCalculator.Enitites import Roman
from GlobeCurrencyCalculator.HelperModule import List


class RomanNumericProvider:
    __values = List()
    __values.extend(
        [
            Roman('I', 1),
            Roman('V', 5),
            Roman('X', 10),
            Roman('L', 50),
            Roman('C', 100),
            Roman('D', 500),
            Roman('M', 1000)
        ])

    def __init__(self):
        pass

    def GetNumericValue(self, romanStr):
        return self.__values.FirstOrDefault(self.__filter, romanStr.upper())

    def GetRomanNumber(self, number):
        pass

    def __filter(self, roman, compareVal):
        if roman.RomanNumber == compareVal:
            return True
        else:
            return False