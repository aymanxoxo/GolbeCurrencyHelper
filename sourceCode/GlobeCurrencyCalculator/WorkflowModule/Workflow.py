from GlobeCurrencyCalculator.AnalysisModule import Analysis
from abc import ABC, abstractmethod

class Workflow(ABC):
    
    def __init__(self, input):
        self.InputEntity = input
        self.Analysis = Analysis()

    @abstractmethod
    def Handle(self):
        pass

    def convertSynonumsToRomans(self, string):
        unitsCountInRomanNumber = ""

        for synonumStr in string:
            s = self.Analysis.GetRomanSynonum(synonumStr)
            if s != None:
                unitsCountInRomanNumber += s.RomanNumber

    
    def ExtractOreAndSynonums(self, string):
        parts = string.split(' ')
        oreName = parts[len(parts) - 1: 1].strip()

        synonumsStr = parts[:len(parts) - 1]
        return [oreName, self.convertSynonumsToRomans(synonumsStr)]
