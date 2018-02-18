from GlobeCurrencyCalculator.HelperModule import InputHelper
from GlobeCurrencyCalculator.AnalysisModule import Analysis

inputHelper = InputHelper()
analysis = Analysis()

lines = inputHelper.ReadLines()

for line in lines:
    input = analysis.DefineSentectType(line)
    input.Workflow.Handle()