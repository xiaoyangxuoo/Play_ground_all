text1 = input("Enter your text1: ")
text2 = input("Enter your text2: ")

try:
    assert text1 and text2
    t1  = text1.lower()
    t2  = text2.lower()

    t1.replace(" ", "")
    t2.replace(" ", "")
    t11 = ''.join(sorted(t1))
    t22 = ''.join(sorted(t2))

    if t11 == t22:
        print("Yes")
    else:
        print("No")
except AssertionError:
    print("No")