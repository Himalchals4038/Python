try:
    a = int(input("Enter a number: "))
    b = 1/a
    print(b)

except ValueError as e:
    print("Please enter a valid value")
    print(e)

except ZeroDivisionError as e:
    print("Make sure division by zero is not occurring")
    print(e)
    
except TypeError as e:
    print("Make sure you are dividing numbers only")
    print(e)

except MemoryError as e:
    print("Memory Full")
    print(e)

except Exception as e:
    print("Unknown error type")
    print(e)
