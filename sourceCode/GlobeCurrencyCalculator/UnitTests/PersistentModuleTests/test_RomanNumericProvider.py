from GlobeCurrencyCalculator.PersistentModule import RomanNumericProvider
from GlobeCurrencyCalculator.Enitites import Roman
import unittest
import sys

sys.path.append('.')

class RomanNumericProviderTests(unittest.TestCase):
    def test_getNumericValue_returnCorrectResult(self):
        provider = RomanNumericProvider()
        result = provider.GetNumericValue(Roman('I', 0))
        print(result.Value)
        # self.assertEqual(result.Value, 1)