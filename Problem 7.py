import math

def primeCheck(num):
    primeCheck = True
    for number in range(2, int(math.floor(num/2))+1): #range in which a num can be checked if prime or not
        if num % number == 0:
            primeCheck = False
            break
    if primeCheck == True:
        return(num)





#Takes in a number and finds which prime it corresponds to if all nums before it were prime
def primeCalc(num):
    currentNum = 2 # number we are checking as prime
    primeCounter = 0 # counts how many primes have been found

    while primeCounter < num:
        primeCheckVar = primeCheck(currentNum)
        if type(primeCheckVar) == int:
            primeCounter += 1
            biggestKnownPrime = primeCheckVar
        currentNum += 1

    print(biggestKnownPrime)
    print(primeCounter)

primeCalc(10001)

