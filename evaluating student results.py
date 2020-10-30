import os
class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        self.message = message


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        self.message = message

d = {}
path = input("Desired location?: ")
file = open(path, 'r')
file_read = file.readlines()

def calculate(line):
    if line.isspace():
        raise BadLine('This is an empty line')
    if line.isalnum():
        if os.stat(path).st_size == 0:
            raise FileEmpty('This is empty file')
        (first_name, last_name, score) = line.split()
        if (first_name + " " + last_name) in d.keys():
            d[first_name + " " + last_name] = float(score) + d.get(first_name + " " + last_name)
        else:
            d[first_name + " " + last_name] = float(score)
    else:
        raise BadLine('This line contains non-supported entries')

for line in file_read:
    try:
        calculate(line)
    except FileEmpty as FE:
        print(FE, ":", FE.message)
    except BadLine as BL:
        print(BL, ":", BL.message)



file.close()
print(d)
# for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
# 	try:
# 		makePizza(pz, ch)
# 	except TooMuchCheeseError as tmce:
# 		print(tmce, ':', tmce.cheese)
# 	except PizzaError as pe:
# 		print(pe, ':', pe.pizza)