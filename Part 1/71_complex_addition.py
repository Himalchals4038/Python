class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __add__(self, c):
        return Complex(self.real + c.real, self.img + c.img)
    
    def __sub__(self, c):
        return Complex(self.real - c.real, self.img - c.img)
    
    def __mul__(self, c):
        mulReal = self.real*c.real - self.img*c.img
        mulImg = self.real*c.img + self.img*c.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.img<0:
            return f"{self.real} - {-self.img}i"
        else:
            return f"{self.real} + {self.img}i"

c1 = Complex(15, 23)
c2 = Complex(7, 39)
cSum = c1 + c2
print(cSum)
cSub = c1 - c2
print(cSub)
cMul = c1 * c2
print(cMul)

