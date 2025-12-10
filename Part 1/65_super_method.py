class Person:
    salary = 500
    country = "India"
    
    def __init__(self):
        print("Initializing Person...")
    def countryInfo(self):
        print(f"This person lives in {self.country}")
    def getSalary(self):
        print(f"Salary of the person is {self.salary}")
    def takeLeave(self):
        print("The person is taking a leave")

class Employee(Person):
    company = "Eternal"
    salary = 1500
    
    def __init__(self):
        super().__init__()
        print("Initializing Employee...")
    def companyInfo(self):
        print(f"This employee works for {self.company}")
    def getSalary(self):
        print(f"Salary of the employee is {self.salary}")
    def takeLeave(self):
        print("The employee is taking a leave")

class Programmer(Employee):
    department = "Frontend"
    salary = 2500
    
    def __init__(self):
        super().__init__()
        print("Initializing Programmer...")
    def departmentInfo(self):
        print(f"The person works in {self.department} department")
    def getSalary(self):
        print(f"Salary of the programmer is {self.salary}")
    def takeLeave(self):
        super().takeLeave()
        print("The programmer is taking a leave")

Arun = Programmer()
Arun.countryInfo()
Arun.companyInfo()
Arun.departmentInfo()
Arun.getSalary()
Arun.takeLeave()

print("\n")

Vijay = Employee()
Vijay.countryInfo()
Vijay.companyInfo()
Vijay.getSalary()
Vijay.takeLeave()

print("\n")

Payal = Person()
Payal.countryInfo()
Payal.getSalary()
Payal.takeLeave()

