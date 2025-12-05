class Employee:
    company = 'Google'
    salary = 12500

Admin = Employee()
Person1 = Employee()
Person2 = Employee()
print(Admin.company)

#Class Attributes
Employee.company = 'Wipro' #Alters the default class data
print(Admin.company) 

#Instance Attributes
Admin.company = 'Zoho' #Alters only the user data
print(Admin.company)

# print(Person1.salary)
# print(Person2.salary)
Person1.salary = 15000
# Person2.salary = 20000
print(Person1.salary)
print(Person2.salary)

