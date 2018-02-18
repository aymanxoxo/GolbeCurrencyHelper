from GlobeCurrencyCalculator.PersistentModule import OreProvider
from GlobeCurrencyCalculator.Enitites import Ore
import unittest

class OreProviderTests(unittest.TestCase):
    def test_addOre_getOre(self):
        provider = OreProvider()
        provider.Add(Ore('gold', 3))
        result = provider.Get('Gold')
        self.assertEqual(result.Value, 3)