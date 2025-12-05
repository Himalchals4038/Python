class Employee:
    company = "Accenture"

    def getInfo(self):
        print("Retrieving Employee Details")

#Example of single inheritance
class Programmer(Employee):
    language = "Python"
    def getLanguage(self):
        print(f"Language used is {self.language}")

    def getInfo(self):
        print("Retrieving Programmer Details")
        
e = Employee()
e.getInfo()
p = Programmer()
p.getInfo()
print(p.company)


