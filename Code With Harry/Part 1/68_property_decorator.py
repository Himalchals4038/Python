class Employee:
    company = "HPCL"
    salary = 6800
    bonus = 623
    
    # def totalSalary(self):
    #     return self.salary + self.bonus
    
    @property
    def totalSalary(self):
        return self.salary + self.bonus
    #Define a function as a property inside a class
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.bonus = val - self.salary
    #Alter class attributes from the property defined earlier

Anuj = Employee()
print(Anuj.totalSalary)
# print(Anuj.totalSalary())

Anuj.salary = 7500
Anuj.bonus = 580
print(Anuj.totalSalary)
# print(Anuj.totalSalary())

Vaishali = Employee()
Vaishali.totalSalary = 8000
print(Vaishali.salary)
print(Vaishali.bonus)

