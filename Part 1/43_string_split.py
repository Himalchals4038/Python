def remove_split(string, word):
    new_string = string.replace(word, "")
    return new_string.split()
text1 = "   This is a sample text   "
new = remove_split(text1, "This")
print(new)



