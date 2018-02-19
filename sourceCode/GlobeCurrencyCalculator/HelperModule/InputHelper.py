from sys import stdin

class InputHelper:
    
    def ReadLine(self):
        line = stdin.readline()
        line = self.__removeSpacesFromLine(line)
        return line

    def ReadLines(self):
        print("please enter all the inputs in lines then Ctrl + Z to submit.")
        lines = stdin.readlines()
        cleanLines = self.__removeSpacesFromLines(lines)
        return cleanLines

    def ReadFile(self):
        print("What is the file name?")
        fname = self.ReadLine()
        nameParts = fname.split('.')
        if len(nameParts) != 2:
            raise ValueError
        if nameParts[-1].lower() != 'txt':
            raise ValueError

        with open(fname) as f:
            lines = f.readlines()
            cleanLines = self.__removeSpacesFromLines(lines)
            return cleanLines

    def __removeSpacesFromLine(self, line):
        line = line.replace('\n', '')
        return line

    def __removeSpacesFromLines(self, lines):
        cleanLines = []
        for line in lines:
            cleanLines.append(self.__removeSpacesFromLine(line))
        return cleanLines