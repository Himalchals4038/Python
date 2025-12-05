class Employee:
    company = "Microsoft"
    def getSalary (self, signature):
        # print("Salary is $150k")
        print(f"Salary of the employee working in {self.company} is {self.salary}\n{signature}")

Admin = Employee()
Admin.salary = 15000
# Employee.getSalary(Admin)
Admin.getSalary("Administrator")




