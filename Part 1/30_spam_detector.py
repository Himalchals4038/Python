text = str(input("Enter the text: "))
spam = ["subscribe here", "money", "buy now", "get views", "click this", "promote"]
s = 0

for i in range (len(spam)):
    if (spam[i] in text):
        s+=1
    else:
        pass
if (s>0):
    print("This message is spam with", s, "instances of spam words")
else:
    print("This message is not spam")


