import unittest
from GlobeCurrencyCalculator.ProcessingModule import SplitterProcessor
from GlobeCurrencyCalculator.Enitites import StoryOre
import sys

sys.path.append('.')


class SplitterProcessorTests(unittest.TestCase):
    def test_SplitSentence_normalBehavior(self):
        splitter = SplitterProcessor()
        storyOre = StoryOre('', '')
        storyOre.Sentence = 'globe is I'
        storyOre = splitter.SplitSentence(storyOre, 'is')
        self.assertEqual(storyOre.LeftPart, 'globe')
        self.assertEqual(storyOre.RightPart, 'I')