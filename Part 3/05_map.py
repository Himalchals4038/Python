def square(num):
    return num**2

list1 = [16, 28, 37, 49]
list2 = []

#Method 1
for i in list1:
    list2.append(square(i))
print(list2)

#Method 2
print(list(map(square, list1)))


