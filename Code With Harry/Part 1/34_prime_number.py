a = int(input("Enter the number: "))
b = 0
if (a==0):
    print("Can't be determined")
elif(a==1 or a==2):
    print("The number is prime")
else:
    for i in range (2, a):
        if (a%i==0):
            b=1
            break
    if(b==1):
        print("The number is not prime")
    else:
        print("The number is prime")

