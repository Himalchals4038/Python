def increment (num):
    try:
        return int(num) + 1
    except:
        raise ValueError ("Please enter another value")

print(increment(15))
print(increment('abg'))




