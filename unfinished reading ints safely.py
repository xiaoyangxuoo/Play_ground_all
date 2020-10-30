def readint(prompt, min, max):
#
    Doit = True
    while Doit:
        try:
            v = int(input(prompt))
            Doit = False
        except ValueError:
            print("Error wrong input")
        except:
            
# put your code here
    return v

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)