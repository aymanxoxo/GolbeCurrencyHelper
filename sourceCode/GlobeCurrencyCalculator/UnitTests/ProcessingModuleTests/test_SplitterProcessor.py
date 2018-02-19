import unittest
from ProcessingModule import SplitterProcessor
from Enitites import StoryOre


class SplitterProcessorTests(unittest.TestCase):
    def test_SplitSentence_normalBehavior(self):
        splitter = SplitterProcessor()
        storyOre = StoryOre('', '')
        storyOre.Sentence = 'globe is I'
        storyOre = splitter.SplitSentence(storyOre, 'is')
        self.assertEqual(storyOre.LeftPart, 'globe')
        self.assertEqual(storyOre.RightPart, 'I')

    def test_SplitSentence_throwValueError(self):
        splitter = SplitterProcessor()
        storyOre = StoryOre('', '')
        storyOre.Sentence = 'Hello World'
        try:
            storyOre = splitter.SplitSentence(storyOre, 'is')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        except:
            self.assertTrue(False)