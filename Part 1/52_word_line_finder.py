content = True
i = 1
word = str(input("Enter word to be searched: "))
with open('log.txt') as f:
    while content:
        content = f.readline()
        if word in content.lower():
            print(content)
            print(f"Yes {word} is present on line number {i}")
        i+=1


