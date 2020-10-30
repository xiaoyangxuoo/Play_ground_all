from pprint import pprint

L1 = input("Enter the first line: ")
L2 = input("Enter the first line: ")
L3 = input("Enter the first line: ")
L4 = input("Enter the first line: ")
L5 = input("Enter the first line: ")
L6 = input("Enter the first line: ")
L7 = input("Enter the first line: ")
L8 = input("Enter the first line: ")
L9 = input("Enter the first line: ")

try:
    assert len(L1) == len(L2) == len(L3) == len(L4) == len(L5) == len(L6) == len(L7) \
           == len(L8) == len(L9) == 9
    if len(L1) == len(set(L1)) and len(L2) == len(set(L2)) and len(L3) == len(set(L3)) and \
            len(L4) == len(set(L4)) and len(L5) == len(set(L5)) and len(L6) == len(set(L6)) and \
            len(L7) == len(set(L7)) and len(L8) == len(set(L8)) and len(L9) == len(set(L9)):
        Big = [list(L1), list(L2), list(L3), list(L4), list(L5), list(L6), list(L7), list(L8), list(L9)]
        set1 = set()
        set2 = set()
        set3 = set()
        set4 = set()
        set5 = set()
        set6 = set()
        set7 = set()
        set8 = set()
        set9 = set()
        for i in range(3):
            for j in range(3):
                set1.add(Big[i][j])
        for i in range(3):
            for j in range(3, 6):
                set2.add(Big[i][j])
        for i in range(3):
            for j in range(6, 9):
                set3.add(Big[i][j])
        for i in range(3, 6):
            for j in range(3):
                set4.add(Big[i][j])
        for i in range(3, 6):
            for j in range(3, 6):
                set5.add(Big[i][j])
        for i in range(3, 6):
            for j in range(6, 9):
                set6.add(Big[i][j])
        for i in range(6, 9):
            for j in range(3):
                set7.add(Big[i][j])
        for i in range(6, 9):
            for j in range(3, 6):
                set8.add(Big[i][j])
        for i in range(6, 9):
            for j in range(6, 9):
                print(Big[i][j])
                print(set9)
                set9.add(Big[i][j])
        print(set9)
        print(len(set9))
        if len(set1) == len(set2) == len(set3) == len(set4) == len(set5) == len(set6) == len(set7) == len(set8) == len(
                set9) == 9:
            print("Yes!")
        else:
            print("No！")
    else:
        print("NO!")

except:
    print("Input error, not 9 digits for each line")


