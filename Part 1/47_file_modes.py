# file = open('sample.txt', 'r')
# data = file.read()
# print(data)
#Read just reads the content of the file

# file = open('sample2.txt', 'w')
# file.write("Hello")
# file.close()
#Write removes existing content from the file and writes the content given

# file = open('sample2.txt', 'a')
# file.write("\nHow are you?")
# file.close()
#Append adds the given content to the end of the already existing content in the file

file = open('sample2.txt', 'a+')
data = file.read()
print(data)
file.write("\nNice to meet you!")
data = file.read()
print(data, end="")
file.close()
#"+" allows both reading and writing/appending the current document

# file = open('sample2.txt', 'w+')
# data = file.read()
# print(data)
# file.write("\nNice to meet you!")
# data = file.read()
# print(data, end="")
# file.close()


