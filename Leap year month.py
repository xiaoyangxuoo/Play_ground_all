def isYearLeap(year):
#
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
# put your code here




def daysInMonth(year, month):
    Odyrdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    Lpyrdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    if isYearLeap(year):
        return Lpyrdays [month-1]
    else:
        return Odyrdays [month-1]
#
# put your new code here

#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")