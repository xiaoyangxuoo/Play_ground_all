def isPrime(num):
    if num == 2:
        return True
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True
        

# put your code here
#
#print(range(1,20))
#print(isPrime(9))
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()