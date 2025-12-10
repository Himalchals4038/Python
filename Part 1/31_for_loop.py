for i in range (1, 14, 2):
    print(i)
else:
    print("Else")

for i in range(12):
    if(i<3):
        pass
    elif(i>9):
        print("Breaking the loop")
        break
    else:
        if (i==5):
            continue
        print(i)


