import math

def is_prime(n):
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

primeNumber = 1
n = 1

while primeNumber < 3000:
	if is_prime(primeNumber):
		print n, primeNumber
		n += 1
	primeNumber +=1
