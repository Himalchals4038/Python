def prime_number(num):
    if (num==0):
        return False
    elif (num==1 or num==2):
        return True
    else: 
        i = 0
        for j in range(2, num):
            if num%j==0:
                i+=1
        if i!=0:
            return False
        else:
            return True

list1 = [18, 61, 42, 73, 50, 33, 47]

#Method 1
list2 = []
for i in list1:
    if prime_number(i)==True:
        list2.append(i)
print(list2)

#Method 2
print(list(filter(prime_number, list1)))

