a = [2, 15, 63, 9, 70, 25]
print(a, type(a))
print(a[3])
a[2] = 22 #List data can be altered
print(a)

b = [15, "Sargam", 63.2, "Sikh"]
print(b, type(b))
b[1] = False
print(b)
for i in range (0,len(b)):
    print(b[i], type(b[i]))

c = ["Sitar", "Veena", "Tabla", "Harmonium", "Gramophone", "Violin", "Banjo", "Guitar", "Drum"]
print(c[:6])
print(c[2:8])
print(c[0:5:2])
print(c[-7:-1:2])



