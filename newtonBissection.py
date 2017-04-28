def newton(num):
    epsilon = 0.01
    i = 0
    guess = num/2.0
    while abs(guess*guess - num) >= epsilon:
        i += 1
        guess = guess - (((guess**2) - num)/(2*guess))
    return i

def bissection(num):
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0, num)
    ans = (high + low)/2.0
    while abs(ans**2 - num) >= epsilon:
        #print('low =', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if ans**2 < num:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return numGuesses

bissectionIsBetter = True
if newton(25) < bissection(25):
    bissectionIsBetter = False
    print(newton(25))
    print(bissection(25))
    print(bissectionIsBetter)

