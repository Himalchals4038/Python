with open ('censor.txt') as f:
    content = f.read()

censorList = ['shit', 'moron', 'fucking', 'donkey', 'bitch', 'fuck', 'nigger', 'ass', 'hell']
for i in range (len(censorList)):
    if censorList[i] in content.lower(): #lower() converts whole text into lowercase
        content = content.replace(censorList[i], "@#$%^&")
with open('censor.txt', 'w') as f:
    f.write(content)

