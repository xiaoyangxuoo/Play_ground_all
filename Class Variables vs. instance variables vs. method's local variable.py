class ExampleClass:
    varia = 1
    def __init__(self, val):
        varia = val
        self.varia = val
        ExampleClass.varia = val
        

print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)

print(ExampleClass.__dict__)
print(exampleObject.__dict__)