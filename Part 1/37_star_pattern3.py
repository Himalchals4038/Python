a = int(input("Enter number of rows to be printed: "))
c = 2*a-1
for i in range(a):
    for j in range(i):
        print(" ", end="")
    for k in range(c):
        print("*", end="")
        c-=2
    print("\n")

