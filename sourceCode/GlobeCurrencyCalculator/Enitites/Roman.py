from Enitites import Input

class Roman(Input):
    def __init__(self, romanNumber, value):
        self.RomanNumber = romanNumber
        self.Value = value if value != None else 0
        
    