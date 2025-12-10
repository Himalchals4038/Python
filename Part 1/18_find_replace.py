sample = "This  is a sample  text,  to be    used for educational    purposes only"
# doubleSpaces = sample.find("  ")
# print(doubleSpaces)
i = 1
while(i>0):
    doubleSpaces = sample.find("  ")
    if doubleSpaces>0:
        sample = sample.replace("  ", " ")
    else:
        i=0
print(sample)
