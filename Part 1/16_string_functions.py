sample = "this is a sample text used for understanding the string functions"
print(len(sample))
print(sample.endswith("none"))
print(sample.endswith("ions"))
print(sample.count("a"))
print(sample.count("st"))
print(sample.capitalize())
print(sample.find("the")) #Finds and returns the position of the first occurrence of the string
print(sample.find("him")) #Returns -1 if not found
print(sample.replace("sample", "made-up")) #Replaces all occurrences of the replaceable string

