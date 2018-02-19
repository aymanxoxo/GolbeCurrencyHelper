from HelperModule import InputHelper
from AnalysisModule import Analysis

inputHelper = InputHelper()
analysis = Analysis()

print("Hello, do you have some calculations for me?")
lines = inputHelper.ReadFile()

for line in lines:
    entity = analysis.DefineSentectType(line)
    print(entity.Workflow.Handle())


print("see you!")