a = [25, 1, 96, 0, 4, 83, 99, 21, 17, 46]
a.sort() #Arranges the elements in the list in ascending order
print(a)
print(sum(a))
b = [25, 1, 96, 0, 4, 83, 99, 21, 17, 46]
b.reverse() #Reverses the sequence of the whole list
print(b)
c = [25, 1, 96, 0, 4, 83, 99, 21, 17, 46]
c.append(62) #Appends 62 to the last of the list
print(c)
c.append(20) #Appends 20 to the last of the list
print(c)
d = [25, 1, 96, 0, 4, 83, 99, 21, 17, 46]
d.insert(3, 15) #Inserts 15 at index number 3 in the list
print(d)
e = [25, 1, 96, 0, 4, 83, 99, 21, 17, 46]
print(e.pop(4)) #Determines element at that index, removes it from the list and returns its value
print(e)
f = [25, 1, 96, 0, 4, 83, 99, 21, 17, 46] #Removes the specified element from the list
f.remove(83)
print(f)
