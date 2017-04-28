'''
Write a problem that asks the User to input ten ints, and then prints the largest odd number.
If no odd number are entered it should write a message to that effect.
'''

intList = []
biggestOdd = 0
i = 1
while i < 11:
    intList.append(int(input("Please write down an Integer: ")))
    i +=1

for num in intList:
    if num % 2 != 0 and num > biggestOdd:
        biggestOdd = num

if biggestOdd == 0:
    print("No odd numbers were inputed.")

else:
    print("The biggest inputed odd number was {}".format(str(biggestOdd)))