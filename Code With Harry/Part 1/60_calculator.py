class Calculator:
    # def __init__(admin, num):
    #     admin.number = num
    def __init__(self, num):
        self.number = num

    def square(self):
        return (self.number**2)

    def cube(self):
        return (self.number**3)

    def squareRoot(self):
        return (self.number**(1/2))

    def cubeRoot(self):
        return (self.number**(1/3))

num = int(input("Enter the number: "))
inputNum = Calculator(num)
print(f"Square of the number is {inputNum.square()}")
print(f"Cube of the number is {inputNum.cube()}")
print(f"Square root of the number is {inputNum.squareRoot()}")
print(f"Cube root of the number is {inputNum.cubeRoot()}")
