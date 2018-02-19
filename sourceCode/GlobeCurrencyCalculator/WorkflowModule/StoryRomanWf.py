from WorkflowModule import Workflow
import PersistentModule
import Enitites

class StoryRomanWf(Workflow):
    
    def Handle(self):
        synonumProvider = PersistentModule.RomanSynonumProvider()
        romanProvider = PersistentModule.RomanNumericProvider()

        if self.InputEntity == None or self.InputEntity.LeftPart == None or self.InputEntity.RightPart == None:
            raise ValueError

        synonumStr = self.InputEntity.LeftPart.strip().upper()
        romanStr = self.InputEntity.RightPart.strip().upper()
        romanVal = romanProvider.GetNumericValue(romanStr)
        roman = Enitites.Roman(romanStr, romanVal)
        romanSynonum = Enitites.RomanSynonym(synonumStr, roman)
        synonumProvider.SetRomanSynonum(romanSynonum)

        return '\n info recorded'
        
    

