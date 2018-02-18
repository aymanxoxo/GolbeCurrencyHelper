from GlobeCurrencyCalculator.Enitites import Input, InputType
from GlobeCurrencyCalculator.PersistentModule import RomanSynonumProvider
from GlobeCurrencyCalculator.PersistentModule import OreProvider
from GlobeCurrencyCalculator.HelperModule import List
from GlobeCurrencyCalculator.Enitites import StoryRoman
from GlobeCurrencyCalculator.Enitites import StoryOre
from GlobeCurrencyCalculator.Enitites import QuestionRoman
from GlobeCurrencyCalculator.Enitites import QuestionOre

class Analysis:
    def DefineSentectType(self, sentence):
        sides = sentence.split('is')
        if len(sides) != 2:
            raise ValueError


        isQuestion = "?" in sentence
        if isQuestion == True:
            sentence = sentence.replace("?", "")
        
        parts = List()
        parts.extend(sentence.split(' '))

        exists = parts.FirstOrDefault(self.__filter, self.IsOre) != None

        if isQuestion:
            if exists:
                questionPhrase = sides[1].replace("?", "")
                q = QuestionOre(questionPhrase)
                q.Type = InputType.QuestionOre
                return q
            else:
                questionPhrase = sides[1].replace("?", "")
                q = QuestionRoman(questionPhrase)
                q.Type = InputType.QuestionRoman
                return q
        else:
            if exists:
                s = StoryOre(sides[0], sides[1])
                s.Type = InputType.StoryOre
                return s
            else:
                s = StoryRoman(sides[0], sides[1])
                s.Type = InputType.StoryRoman
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
    