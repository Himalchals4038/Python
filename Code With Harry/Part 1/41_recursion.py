def factorial_iter(num):
    a = 1
    for i in range(num):
        a*=(i+1)
    return a
# num = int(input("Enter the number: "))
# print(factorial_iter(num))

def factorial_recursive(num):
    if (num == 0 or num == 1):
        return 1
    return num * factorial_recursive(num-1)
num = int(input("Enter the number: "))
print(factorial_recursive(num))

