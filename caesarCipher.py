
def encrypt(str, num):
    originalStr = list(str) # splits up the original string into each char.
    finalStr = '' # where final encoded string will be placed
    for value in originalStr:
        finalStr += chr(ord(value)+num)
    return(finalStr)

def decrypt(str, num):
    originalStr = list(str) # splits up the original string into each char.
    finalStr = '' # where final encoded string will be placed
    for value in originalStr:
        finalStr += chr(ord(value)-num)
    return(finalStr)


print(encrypt('Mo Adib', 5))
#print(decrypt('Hmjjxj%nx%~zrr~', 5))

