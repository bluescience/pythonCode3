def cubeRoot(num):
    ans = 0
    while ans**3 < abs(num):
        ans += 1

    if ans**3 == abs(num):
        return("The perfect cubic root of {} is {}.".format(num, ans))
    else:
        return("There is no perfect root for {}".format(num))


print(cubeRoot(int(input("Input an integer: "))))