def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100!= 0:
        return True
    elif year % 400!= 0:
        return False
    else:
        return True
#
# your code from LAB 4.1.3.6

#
OdyrDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,  30, 31]
LpyrDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31,  30, 31]

def daysInMonth(year, month):
    
    if isYearLeap(year):
        if month in range(1, 13):
            return LpyrDays[month-1]
        else:
            return None
    else:
        if month in range(1, 13):
            return OdyrDays[month-1]#
        else: 
            return None

# your code from LAB 4.1.3.7
#
#print(29 in LpyrDays)

def dayOfYear(year, month, day):
    if isYearLeap(year):
        if month in range(1, 13) and day in LpyrDays:
            if daysInMonth(year, month)!= None:
                return ('Year of ', year, 'Month of ', month, 'Day: ', daysInMonth(year, month))
        else:
            return None
    else:
        if month in range(1, 13) and day in OdyrDays :
            if daysInMonth(year, month) != None:
                return ('Year of ', year, 'Month of  ', month, 'Day: ', daysInMonth(year, month))
        else:
            return None
#
# put your new code here
#print(isYearLeap(2001))

print(dayOfYear(2000, 2, 32))