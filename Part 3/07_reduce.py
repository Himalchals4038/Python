from functools import reduce

sum = lambda a,b: a+b
list1 = [48, 76, 12, 39]

print(reduce(sum, list1))



