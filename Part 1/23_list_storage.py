list1 = []
# a = 1
# i = 1
# while(i>0):
#     number = int(input("Enter number to append: "))
#     list1.append(number)
#     a+=1
#     if(a>10):
#         i-=1
for i in range (10):
    number = int(input("Enter number to append: "))
    list1.append(number)
list1.sort()
print(list1, len(list1))

