hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#
endH = (hour*60 + mins + dura ) // 60 % 24
endM = (hour*60 + mins + dura ) - ((hour*60 + mins + dura ) // 60) * 60

print ('EndTime is ', endH, ' : ', endM)