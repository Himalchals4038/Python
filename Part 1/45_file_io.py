# file = open('sample.txt', 'r')
file = open('sample.txt') #Default mode is 'r'

# data = file.read()
data = file.read(10) #Reads only first 10 characters
#A file can be read only once

print(data)
file.close()


