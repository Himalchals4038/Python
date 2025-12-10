class Person:
    def __init__(self):
        print("Welcome to the interface")
    # @staticmethod
    # def greet():
    #     print("Welcome to the terminal")
    
    salary = 500
    country = "India"
    def countryInfo(self):
        print(f"This person lives in {self.country}")
    def getSalary(self):
        print(f"Salary of the employee is {self.salary}")

class Employee(Person):
    company = "Eternal"
    salary = 1500
    def companyInfo(self):
        print(f"This employee works for {self.company}")
    def getSalary(self):
        print(f"Salary of the employee is {self.salary}")

class Programmer(Employee):
    department = "Frontend"
    salary = 2500
    def departmentInfo(self):
        print(f"The person works in {self.department} department")
    def getSalary(self):
        print(f"Salary of the programmer is {self.salary}")

Arun = Programmer()
# Arun.greet()
Arun.countryInfo()
Arun.companyInfo()
Arun.departmentInfo()
Arun.getSalary()

print("\n")

Vijay = Employee()
# Vijay.greet()
Vijay.countryInfo()
Vijay.companyInfo()
# Vijay.departmentInfo()
Vijay.getSalary()

print("\n")

Payal = Person()
# Payal.greet()
Payal.countryInfo()
# Payal.companyInfo()
# Payal.departmentInfo() 
Payal.getSalary()


