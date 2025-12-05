class Employee:
    company = "Microsoft"
    
    # def __init__(self): #Runs automatically on initiating the class, no separate calling needed
    #     print("Employee ID created")
        
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        print("Employee ID created")
        
    def getDetails (self, signature):
        print(f"Salary of {self.name} working in the {self.department} department is {self.salary}\nThanks: {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

Admin = Employee("Viraj", 2600, "Innovation")
Admin.getDetails("Viraj Mehta")





