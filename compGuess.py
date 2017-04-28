topGuess = 1000000
num = int(input("Please input an int in between 1 and {}: ".format(topGuess)))
compGuess = topGuess // 2


guesses = 0

while compGuess != num:
    if compGuess > num:
        compGuess = compGuess // 2
    elif compGuess < num:
        compGuess = compGuess + compGuess // 2
    print(compGuess)
    guesses +=1

print("Your guess is {} and took {} guesses".format(num, guesses))
