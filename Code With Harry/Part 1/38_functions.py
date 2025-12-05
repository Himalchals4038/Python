def average(marks):
    a = 0
    for i in range (len(marks)):
        a += marks[i]
    b = a/len(marks)
    return b

marks1 = [74, 84, 95, 93, 81, 77]
print(average(marks1))

# def call():
#     return("Hello, how can I help?")
# print(call())
def call():
    print("Hello, how can I help?")
call()

def greet(name):
    print("Good morning, " + name + "\nHow are you?")
print(greet("Robin"))

