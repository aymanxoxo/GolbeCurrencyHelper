from GlobeCurrencyCalculator.WorkflowModule import Workflow
from GlobeCurrencyCalculator.PersistentModule import RomanSynonumProvider, RomanNumericProvider
from GlobeCurrencyCalculator.Enitites import RomanSynonym, Roman

class StoryRomanWf(Workflow):
    
    def Handle(self):
        synonumProvider = RomanSynonumProvider()
        romanProvider = RomanNumericProvider()

        if self.InputEntity == None or self.InputEntity.LeftPart == None or self.InputEntity.RightPart == None:
            raise ValueError

        synonum = self.InputEntity.LeftPart.strip().upper()
        roman = self.InputEntity.RightPart.strip().upper()

        if self.Analysis.IsRomanSynonum(roman) == False:
            raise ValueError
        
        synonumProvider.SetRomanSynonum(RomanSynonym(synonum, Roman(roman, romanProvider.GetNumericValue(roman))))

        return '\n info recorded'
        
    

