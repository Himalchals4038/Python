first = "Hello, "
second = "how are you?"
sum = first + second
# print(sum)
print(first[0])
print(first[1])
print(first[5])
print(sum[15])
print(sum[16])

# sum[5] = "a"
# String item modification not allowed
print(sum[2:10])
# Last digit is excluded and first digit is included
print(first[-2])
print(second[-1])

print(first[:3])
print(second[2:])
print(sum[-8:-2])
print(first[0::2]) #skips every 2nd character
print(first[0:3:2])
print(second[1::3]) #skips every 2 characters in between
