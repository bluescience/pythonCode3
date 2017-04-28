
def getLCM(num):
    i = 1
    staticNum = num + 1 #sets
    while i < staticNum:
        if num % 2 != 0 or num % i != 0:
            num += 1
            i = 1
        else:
            i+=1
    return num

num = getLCM(20)
print(num)