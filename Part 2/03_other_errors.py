try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Index out of range")
    print(e)

try:
    my_dict = {"name": "Harry"}
    print(my_dict["age"])
except KeyError as e:
    print("Key not found in dictionary")
    print(e)

# try:
#     print(undefined_var)
# except NameError as e:
#     print("Variable not defined")
#     print(e)

try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError as e:
    print("File not found")
    print(e)

try:
    text = "hello"
    text.nonexistent_method()
except AttributeError as e:
    print("Attribute does not exist")
    print(e)

# try:
#     import nonexistent_module
# except ModuleNotFoundError as e:
#     print("Module not found")
#     print(e)