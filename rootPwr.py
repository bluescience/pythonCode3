def rootPwr(num):
    rt = 0
    pwr = 6
    while (rt ** pwr) != abs(num):
        rt += 1
        if rt > num-1: # no root is bigger than its num
            pwr -= 1
            rt = 0
            if pwr < 0:
                return("There is no valid solution to this problem.")

    return("The solution for int = {} is root = {} and pwr = {}.".format(num, rt, pwr))

print(rootPwr(int(input("Input an integer: "))))