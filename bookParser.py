import urllib.request
import string

data = urllib.request.urlopen("http://www.gutenberg.org/cache/epub/40929/pg40929.txt")
#Read File
text = data.read().decode('utf-8-sig')

#text = text.split(" ") #removes whitespace
repeatCheck = {} #holds how many repeats of a word there are and counts them.
text = text.split('\n')


for line in text:
    line = line.split(" ")
    #print(line)
    for word in line:
        word = word.strip().strip(string.punctuation).lower() # stripping whitespace, punc, and putting everything to lowercase.
        #print(word)
        if word not in repeatCheck.keys(): #checks repeats and adds the word, and the value 1 to the array if the word is not found
            repeatCheck[word.lower()] = 1

        elif word in repeatCheck: #adds an add
            repeatCheck[word.lower()] += 1

#repeatCheck = list(filter(None, repeatCheck))
#print(repeatCheck)

i = 0
strCheck = []

for value in repeatCheck:
    if type(value) == str:
        strCheck.append(value)

for string in strCheck:
    i += 1
#print(i)

repeatCheck.pop("", None)

value = sorted(repeatCheck.values(), reverse = True)[0:11]
print(value)
for num in value:
    key=list(repeatCheck.keys())[list(repeatCheck.values()).index(num)]
    print(key + " " + str(num))