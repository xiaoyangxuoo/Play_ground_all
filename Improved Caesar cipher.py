text = input("Enter your message: ")
shiftvalue = int(input("Enter your desired shift value: "))
cipher = ''
try:
    assert shiftvalue in range(1, 26)

    for char in text:
        if (ord(char) not in range(65,91)) and (ord(char) not in range(48, 58)) and (ord(char) not in range(97,123)) and char !=" ":
            raise TypeError
        if  char.isspace() or char.isdigit():
            cipher += char
            continue
    #char = char.upper()
        if ord(char)>90:
            code = ord(char) + shiftvalue
            if code > ord('z'):
                code = ord('a')-1 + code - ord('z')
            cipher += chr(code)
        else:
            code = ord(char) + shiftvalue
            if code > ord('Z'):
                code = ord('A') - 1 + code - ord('Z')
            cipher += chr(code)
except TypeError:
    print("Input not valid, please re-enter!")
except AssertionError:
    print("Shift value or not valid please re-enter!")


print(cipher)