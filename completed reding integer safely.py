def readint(prompt, min, max):
    #
    Doit = True
    while Doit:
        try:
            v = int(input(prompt))
            assert v in range(min, max+1)#assert is very useful for making the judgement!
            return v
            Doit = False
        except ValueError:
            print("Error wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range")

    # put your code here
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)