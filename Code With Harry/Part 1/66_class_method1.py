class Employee:
    location = "Gurgaon"
    salary = 500
    position = 3

    def changeSalary(self, newSalary):
        self.salary = newSalary
    
    #Used to alter the class attribute value itself
    def changePosition(self, newPosition):
        self.__class__.position = newPosition

Person1 = Employee()
print(Employee.salary)
print(Employee.position)
print(Person1.salary)
print(Person1.position)

Person1.changeSalary(600)
Person1.changePosition(4)
print(Employee.salary)
print(Employee.position)
print(Person1.salary)
print(Person1.position)


