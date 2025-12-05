part1 = "First Part"
part2 = "Second Part"
part3 = "Third Part"

# a = f"This is the {part1} and this is the {part2}"

a = "This is the {} and this is the {}".format(part1, part2)
print(a)
#Older method to denote a f string

a = "This is the {1} and this is the {0} and rest is {2}".format(part1, part2, part3)
print(a)
a = "This is the {0} and this is the {0}".format(part1, part2)
print(a)
#Sequence of printing can be altered by denoting the index numbers, even same index can be used in multiple places





