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

    def __str__(self):
        return f"Decimal number: {self.num}"

    def __len__(self):
        return f"Length of the number is {len(self.num)}"

n = Number(8)
print(n)
print(len(n))


