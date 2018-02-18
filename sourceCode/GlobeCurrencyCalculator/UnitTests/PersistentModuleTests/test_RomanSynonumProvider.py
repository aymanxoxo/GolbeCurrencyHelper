from GlobeCurrencyCalculator.PersistentModule import RomanSynonumProvider
from GlobeCurrencyCalculator.Enitites import RomanSynonym
from GlobeCurrencyCalculator.Enitites import Roman
import unittest
import sys
sys.path.append('.')

class RomanSynonumProviderTests(unittest.TestCase):
    def test_addSyn_getSyn(self):
        provider = RomanSynonumProvider()
        provider.SetRomanSynonum(RomanSynonym('test', Roman('X', 10)))
        result = provider.GetRoman('Test')
        self.assertEqual(result.RomanNumber, 'X')