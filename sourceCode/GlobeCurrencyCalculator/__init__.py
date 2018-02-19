from HelperModule import InputHelper
from AnalysisModule import Analysis

inputHelper = InputHelper()
analysis = Analysis()

print("Hello, do you have some calculations for me?")
print("What is the file name?")
fileName = inputHelper.ReadLine()
lines = inputHelper.ReadFile(fileName)

for line in lines:
    entity = analysis.DefineSentectType(line)
    print(entity.Workflow.Handle())


print("see you!")