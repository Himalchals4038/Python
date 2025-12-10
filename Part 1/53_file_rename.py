import os

oldName = 'sample3.txt'
newName = 'renamed_by_python.txt'
with open(oldName) as f:
    data = f.read()
with open(newName, 'w') as f:
    f.write(data)

os.remove(oldName)
