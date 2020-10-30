firstr = input("First string: ")
secostr = input("Second string: ")

try:
    assert isinstance(firstr, str) and isinstance(secostr, str)
    idx = 0
    for i in firstr:
        idx = secostr.find(i, idx)
        if idx == -1:
            status = "No"
            break
        status = "yes"
        idx += 1
except:
    print("Input error")

print(status)
            
        
        
    