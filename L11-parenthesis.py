#121910313016
class stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isempty(self):
        return self.items == []

def par_checker(symbol_string):
    s = stack()
    balanced = True
    i = 0
    while i < len(symbol_string) and balanced:
        symbol = symbol_string[i]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isempty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        i = i + 1
    if(balanced and s.isempty()):
        return True
    else:
        return False
def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

print(par_checker('([{}])'))        #Balanced
print(par_checker('({}([])'))       #Unbalanced
