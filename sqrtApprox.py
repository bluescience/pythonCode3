x = -125
lastx = x
x = abs(x)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
if x < 0:
    high = x
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
     print('low =', low, 'high =', high, 'ans =', ans)
     numGuesses += 1
     if ans**3 < x:
        low = ans
     else:
        high = ans
     ans = (high + low)/2.0
if lastx < 0:
    ans = -1 * ans

print('numGuesses =', numGuesses)
print(ans, 'is close to cubic root of', lastx)