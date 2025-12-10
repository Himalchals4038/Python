a = 51 #Global variable
def func1():
    global a #Access and alter global variable value
    print(a)
    a = 26 #Local variable
    print(a)

func1() 
print(a) 



