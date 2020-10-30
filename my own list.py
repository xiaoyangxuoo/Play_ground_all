def mysplit(strng):
    x = []
    if strng.isspace():
        return []
    else:
        fnd = strng.find(" ")
        lst = []
        while fnd != -1:
            lst.append(fnd)
            fnd = strng.find(" ", fnd + 1)
            
        if lst != [] and lst[0] != 0:
                x.append(strng[0:lst[0]])
        for i in range(1, len(lst)):
            if lst[i-1] <= lst[i]+2:
                x.append(strng[lst[i-1]+1:lst[i]])
        
        if lst!= [] and lst[-1] != len(strng)-1:
            x.append(strng[lst[-1]+1:])
        return x 
#

# put your code here
#

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))