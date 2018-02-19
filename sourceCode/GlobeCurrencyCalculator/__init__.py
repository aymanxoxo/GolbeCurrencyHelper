from HelperModule import InputHelper
from AnalysisModule import Analysis

inputHelper = InputHelper()
analysis = Analysis()

print("Hello, do you have some calculations for me?")

exit = 'n'

while exit.lower() != 'y':
    lines = inputHelper.ReadFile()

    if lines != None:
        for line in lines:
            try:
                entity = analysis.DefineSentectType(line)
                print(entity.Workflow.Handle())
            except:
                print("\n sorry my master didn't teach me this :(")
    else:
        print("\n Are you sure you inserted your input? because i got nothing ;)")

    print("\n Do you want to exit? Y/N")
    exit = inputHelper.ReadLine()


print("see you!")