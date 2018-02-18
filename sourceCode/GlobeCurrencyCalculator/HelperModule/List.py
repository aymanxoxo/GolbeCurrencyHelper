

class List(list):
    def FirstOrDefault(self, filter, filterVal):
        for l in self:
            if filter(l, filterVal):
                return l
        return None

    def Where(self, filter, filterVal):
        result = []
        for l in self:
            if filter(l, filterVal):
                result.extend(l)
        return result
