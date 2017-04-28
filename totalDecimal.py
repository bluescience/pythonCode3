s = '1.23,2.4,3.123,8.56,7.8'
sList = s.split(",")
total = 0
for x in sList:
    total += float(x)
print(total)

