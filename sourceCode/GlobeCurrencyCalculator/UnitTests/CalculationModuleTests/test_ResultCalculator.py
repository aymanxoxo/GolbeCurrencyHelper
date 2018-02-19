from CalculationModule import ResultCalculator
from Enitites import Ore
import unittest

class ResultCalculatorTests(unittest.TestCase):
    def test_ResolveOreUnitValue_normalBehavior(self):
        calculator = ResultCalculator()
        result = calculator.ResolveOreUnitValue(2, Ore('gold'), 4)
        self.assertEqual(result.Value, 2)

    def test_CalculateOreUnitsValue_normalBehavior(self):
        calculator = ResultCalculator()
        result = calculator.CalculateOreUnitsValue(2, Ore('gold', 2))
        self.assertEqual(result, 4)