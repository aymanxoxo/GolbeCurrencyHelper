from PersistentModule import RomanSynonumProvider
from Enitites import RomanSynonym
from Enitites import Roman
import unittest

class RomanSynonumProviderTests(unittest.TestCase):
    def test_addSyn_getSyn(self):
        provider = RomanSynonumProvider()
        provider.SetRomanSynonum(RomanSynonym('test', Roman('X', 10)))
        result = provider.GetRoman('Test')
        self.assertEqual(result.RomanNumber, 'X')