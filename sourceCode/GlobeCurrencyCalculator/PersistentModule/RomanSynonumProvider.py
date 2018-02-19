from HelperModule import List
from Enitites import RomanSynonym

class RomanSynonumProvider:
    __synonums = List()
    
    def __init__(self):
        pass
    
    def GetRoman(self, synonumStr):
        return self.__synonums.FirstOrDefault(self.__filter, synonumStr.strip().upper())

    def SetRomanSynonum(self, romanSynonym):
        romanSynonym.Synonum = romanSynonym.Synonum.strip().upper()
        self.__synonums.append(romanSynonym)

    def __filter(self, synonum, synonumStr):
        if synonum.Synonum == synonumStr:
            return True
        else:
            return False
