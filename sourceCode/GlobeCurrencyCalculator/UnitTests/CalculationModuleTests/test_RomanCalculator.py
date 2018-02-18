from GlobeCurrencyCalculator.CalculationModule import RomanCalculator
import unittest

class RomanCalculatorTests(unittest.TestCase):

    calculator = RomanCalculator()

    def test_III_3(self):
        result = self.calculator.CalculatorRomanValue('III')
        self.assertEqual(result, 3)

    def test_VI_6(self):
        result = self.calculator.CalculatorRomanValue('VI')
        self.assertEqual(result, 6)

    def test_IV_4(self):
        result = self.calculator.CalculatorRomanValue('IV')
        self.assertEqual(result, 4)

    def test_XIV_14(self):
        result = self.calculator.CalculatorRomanValue('XIV')
        self.assertEqual(result, 14)

    def test_XVI_16(self):
        result = self.calculator.CalculatorRomanValue('XVI')
        self.assertEqual(result, 16)

    def test_MMMCDXLVI_3446(self):
        result = self.calculator.CalculatorRomanValue('MMMCDXLVI')
        self.assertEqual(result, 3446)

    def test_smann_mmcdxlvt_3446(self):
        result = self.calculator.CalculatorRomanValue('mmmcdxlvi')
        self.assertEqual(result, 3446)

    def test_MMMMI_error(self):
        try:
            result = self.calculator.CalculatorRomanValue('MMMMI')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)
    
    def test_hello_error(self):
        try:
            result = self.calculator.CalculatorRomanValue('hello')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)