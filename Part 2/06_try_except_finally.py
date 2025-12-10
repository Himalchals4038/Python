try:
    i = int(input("Enter a number: "))
    a = 1/i
except Exception as e:
    print(e)
finally:
    print("Code run complete")
#Finally runs at the end whether try passes or exception occurs


