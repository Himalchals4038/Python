try:
    i = int(input("Enter a number: "))
    a = 1/i
except Exception as e:
    print(e)
else:
    print("Code run successfully!")
#Else runs alternate to except
