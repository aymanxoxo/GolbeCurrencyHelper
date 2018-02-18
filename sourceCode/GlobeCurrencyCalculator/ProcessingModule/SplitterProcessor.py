from GlobeCurrencyCalculator.Enitites import Input

class SplitterProcessor:
    def SplitSentence(self, input, separative):
        parts = input.Sentence.split(separative)
        if len(parts) != 2:
            raise ValueError()
        input.LeftPart = parts[0].strip()
        input.RightPart = parts[1].strip()
        return input