'''
def isIn (str1, str2):
    if str1 in str2:
        return True
    elif str2 in str1:
        return True
    else:
        return False
'''
def isIn(str1, str2):

    i = 0 #counter variable, checking to see if values match after the first letter has been found.

    for letter in str1: # checking to see if str2 in str1
        if letter == str2[i]: #checking to see if first letter of str2 can be found in str1
            if str2[-1] == str2[i]: #checking if last value of str2 is equal to the last value found by the iterator. If found, should have iterated with no errors and found the complete string.
                return True
            i += 1
        else:
            i = 0 #resets iterator as soon as there is no longer a match.
    i = 0
    for letter in str2: #same as last.
        if letter == str1[i]: #checking if str1 is in str2
            if str1[-1] == str1[i]: #same as last
                return True
            i += 1  # same as last
        else:
            i = 0 #same as last

    return False #No commonalities should have been located




print(isIn("iuoojuoiaoiu","oiu"))
print(isIn("bhjsahiusaiusa","dsadsadsa"))
print(isIn("k","yuiqaskl"))