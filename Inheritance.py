# Testing properties: instance variables
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__(), #if inheritance needed, this line must be invoked
        self.subVar = 12

obj = Sub()

print(obj.subVar)
#print(obj.supVar)