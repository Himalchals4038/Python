class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("Adding the numbers")
        return self.num + num2.num
    
    def __sub__(self, num2):
        print("Subtracting the numbers")
        return self.num - num2.num
    
    def __mul__(self, num2):
        print("Multiplying the numbers")
        return self.num * num2.num
    
    def __truediv__(self, num2):
        print("Dividing the numbers")
        return self.num / num2.num
    
    def __floordiv__(self, num2):
        print("Box dividing the numbers")
        return self.num // num2.num

n1 = Number(4)
n2 = Number(5)
add = n1 + n2
print(add)
sub = n1 - n2
print(sub)
mul = n1 * n2
print(mul)
truediv = n1 / n2
print(truediv)
floordiv = n1 // n2
print(floordiv)
