from GlobeCurrencyCalculator.AnalysisModule import Analysis
from GlobeCurrencyCalculator.Enitites import StoryRoman
from GlobeCurrencyCalculator.Enitites import StoryOre
from GlobeCurrencyCalculator.Enitites import QuestionRoman
from GlobeCurrencyCalculator.Enitites import QuestionOre
import unittest

class test_Analysis(unittest.TestCase):
    
    analysis = Analysis()

    def test_defineSentenceType_StoryRoman(self):
        result = self.analysis.DefineSentectType('globe is I')
        self.assertIsInstance(result, StoryRoman)
    
    def test_defineSentenctType_StoryOre(self):
        result = self.analysis.DefineSentectType('globe gold is 32 credits')
        self.assertIsInstance(result, StoryOre)

    def test_defineSentenceType_QuestionRoman(self):
        result = self.analysis.DefineSentectType('how much credits is globe globe?')
        self.assertIsInstance(result, QuestionRoman)

    def test_defineSentenctType_QuestionOre(self):
        result = self.analysis.DefineSentectType('how much credits is globe gold?')
        self.assertIsInstance(result, QuestionOre)    
