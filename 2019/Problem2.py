import math

#Find all primes below 1000
primes = []
isPrime = 0
for primeCounter in range(1, 2000):
    isPrime = 0
    for primeCounter2 in range(1, primeCounter + 1):
        if primeCounter % primeCounter2 == 0:
            isPrime += 1

    if isPrime == 2:
        primes.append(primeCounter)

def FindPrimes(mean):
    for primeNum in primes:
        if primeNum > 2 * mean:
            break
        
        prime2 = ((2 * mean) - primeNum)
        if prime2 in primes:
            return [primeNum, prime2]
        
    


for number in range(1, 1000):
    averagePrimes = FindPrimes(number)
    if averagePrimes is not None:
        print("%s: %s %s" % (number, averagePrimes[0], averagePrimes[1]))
    else:
        print("Not possible for %s" % (number))



