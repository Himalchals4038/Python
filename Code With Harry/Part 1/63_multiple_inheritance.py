class Employee:
    company = "MasterCard"
    eCode = 52

class Programmer:
    company = "GeeksForGeeks"
    level = 0

# class FreeLancer(Employee, Programmer):
class FreeLancer(Programmer, Employee):
    name = "Mohan"
    
    def upgradeLevel(self):
        self.level+=1

Person1 = FreeLancer()
print(Person1.name)
print(Person1.company)
print(Person1.eCode)
print(Person1.level)

Person1.upgradeLevel()
print(Person1.level)


