import random
b = 0
d = 0
f = 0
while (True):
    q = random.randint(15, 20)
    a = input("Enter a number: ")
    try:
        a = int(a)
        if a == q:
            print("Correct Guess :)")
            f += 1
        else:
            print("Wrong pick :(, better luck next time")
    except Exception as e:
        print("Wrong input, try again!")
        continue
    while(True):
        c = input("Do you want to continue (y/n): ")
        try:
            c = str(c)
            if c == 'y':
                break
            elif c == 'n':
                d = 1
                break
            else:
                print("Wrong input, try again!")
                continue
        except Exception as e:
            print("Wrong input, try again!")
            continue
    if d == 1:
        break
    else:
        b += 1
        continue
print(f"No. of attempts taken: {b}")
print(f"No. of correct guesses: {f}")
