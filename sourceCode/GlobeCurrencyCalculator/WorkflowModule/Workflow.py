import AnalysisModule
from abc import ABC, abstractmethod

class Workflow(ABC):
    
    def __init__(self, input):
        self.InputEntity = input
        self.Analysis = AnalysisModule.Analysis()

    @abstractmethod
    def Handle(self):
        pass

    def convertSynonumsToRomans(self, string):
        unitsCountInRomanNumber = ""

        for synonumStr in string.split(' '):
            s = self.Analysis.GetRomanSynonum(synonumStr)
            if s != None:
                unitsCountInRomanNumber += s.RomanNumber

        return unitsCountInRomanNumber

    
    def ExtractOreAndSynonums(self, string):
        parts = string.split(' ')
        oreName = parts[-1].strip()

        synonumsStr = string.replace(oreName, '')
        return [oreName, self.convertSynonumsToRomans(synonumsStr)]
