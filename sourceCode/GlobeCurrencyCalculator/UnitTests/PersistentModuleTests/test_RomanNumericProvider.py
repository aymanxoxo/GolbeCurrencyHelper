from GlobeCurrencyCalculator.PersistentModule import RomanNumericProvider
from GlobeCurrencyCalculator.Enitites import Roman
import unittest

class RomanNumericProviderTests(unittest.TestCase):
    def test_getNumericValue_returnCorrectResult(self):
        provider = RomanNumericProvider()
        result = provider.GetNumericValue('I')
        self.assertEqual(result.Value, 1)