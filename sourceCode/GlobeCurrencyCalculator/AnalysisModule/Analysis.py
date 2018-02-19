from PersistentModule import RomanSynonumProvider, OreProvider
from HelperModule import List
import Enitites

class Analysis:
    def DefineSentectType(self, sentence):
        sides = sentence.split(' is ')
        if len(sides) != 2:
            raise ValueError


        isQuestion = "?" in sentence
        if isQuestion == True:
            sentence = sentence.replace("?", "")
        
        parts = List()
        parts.extend(sentence.split(' '))

        

        if isQuestion:
            questionPhrase = sides[1].replace("?", "")
            if parts.FirstOrDefault(self.__filter, self.IsOre) != None:
                q = Enitites.QuestionOre(questionPhrase)
                q.Type = Enitites.InputType.QuestionOre
                return q
            else:
                q = Enitites.QuestionRoman(questionPhrase)
                q.Type = Enitites.InputType.QuestionRoman
                return q
        else:
            if parts.FirstOrDefault(self.__filter, self.IsRomanSynonum) != None:
                s = Enitites.StoryOre(sides[0], sides[1])
                s.Type = Enitites.InputType.StoryOre
                return s
            else:
                s = Enitites.StoryRoman(sides[0], sides[1])
                s.Type = Enitites.InputType.StoryRoman
                return s

    def __filter(self, str, func):
        return func(str)
            
    def IsRomanSynonum(self, str):
        romanProvider = RomanSynonumProvider()
        result = romanProvider.GetRoman(str)
        return False if result == None else True

    def GetRomanSynonum(self, str):
        romanProvider = RomanSynonumProvider()
        result = romanProvider.GetRoman(str)
        return result

    def IsOre(self, str):
        if not str or len(str.strip()) == 0:
            return False
        oreProvider = OreProvider()
        result = oreProvider.Get(str.strip())
        x = False if result == None else True
        return x