a = set()
a.add(15)
a.add(36)
a.add(73)
a.add(55)
a.add(69)
a.add(41)
print(a)

# a.add([7, 9, 4]) 
# #List cannot be added to a set

a.add((5, 9, 3)) #Tuple can be added to a set
print(a)

# a.add({
#     "Python" : "Language1",
#     "JavScript" : "Language2"
# })
#Dictionary can't be added to a set
print(len(a))

a.remove(15)
print(a)
# a.remove(26) #Throws error if element is not present in the set

print(a.pop()) #Removes a random value from the set
print(a)

a.clear() #Empties the set
print(a)

s1 = {13, 24, 39, 57, 66, 82, 95, 71, 46}
s2 = {36, 49, 76, 52, 66, 82, 24}
print(s1.union({11, 49}))
print(s2.intersection({52, 24, 63, 85}))

s3 = set()
s3.add(18)
s3.add('18')
s3.add(18.0)
print(len(s3))
#Set consider all numbers as float values


