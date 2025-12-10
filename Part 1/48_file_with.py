with open('sample3.txt', 'r') as f:
    a = f.read()
print(a) #Prints the content in file
with open('sample3.txt', 'w') as f:
    a = f.write("Here is something to think on")
print(a) #Prints length of content inserted






