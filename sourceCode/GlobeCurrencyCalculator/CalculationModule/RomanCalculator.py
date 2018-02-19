import PersistentModule
import re

class RomanCalculator:
    def CalculatorRomanValue(self, romanStr):
        if self.__isValidRoman(romanStr) == False:
            raise ValueError

        result = 0
        index = 0
        if len(romanStr) == 1:
            first = self.__getNumeric(romanStr[index])
            result = result + first
        else:
            while index < len(romanStr) - 1:
                first = self.__getNumeric(romanStr[index])
                second = self.__getNumeric(romanStr[index+1])
                if self.__canBeSubtracted(first, second):
                    result = result + (second - first)
                    index = index + 2
                else:
                    result = result + first
                    index = index + 1
                    if index == len(romanStr) - 1:
                        result = result + second
        return result
            
    def __isValidRoman(self, romanStr):
        result = re.search('(?:(i){4}|(x){4}|(c){4}|(m){4})', romanStr.lower())
        if result == None:
            return True
        else:
            return False

    def __getNumeric(self, roman):
        provider = PersistentModule.RomanNumericProvider()
        result = provider.GetNumericValue(roman)
        if result == None:
            raise ValueError
        return result

    def __canBeSubtracted(self, first, second):
        if self.__startWith5(first) == False and (first * 5 == second or first * 10 == second):
            return True
        return False

    def __startWith5(self, num):
        numStr = str(num)
        firstDigit = numStr[:1]
        return firstDigit == "5"

    def __isNumber(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False