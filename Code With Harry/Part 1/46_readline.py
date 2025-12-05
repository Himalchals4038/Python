file = open('sample.txt')
data = file.readline()
print(data, end="")
data = file.readline()
print(data)
#Readline reads one line of the file at a time
file.close()




