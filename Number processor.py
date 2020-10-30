# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    assert not line.isspace()
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except AssertionError:
    print("You haven't enter a number")
except:
    print(substr, "is not a number.")