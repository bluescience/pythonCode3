class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

class Simple(Complex):
    def __init__(self, realpart, imagpart, money):
        self.r = 100

        self.money = money

Jeremy = Complex(9, "i")
print(Jeremy.r)

bob = Simple(3, "cool", 981289321080921830921219083219803219098321)

print(bob.r)
print(bob.money)

tel = {"jack": 54434, "jajnc": 902910}
print(tel["jack"])

l = ("kac", 190, True, (8, "Jeremy"), 7.0)
for x in l:
    print(x)