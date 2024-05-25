#Multiple inheritance
# a one Child class inherits from multiple parent classes.
# It means the child class has access to all the parent classes' methods and attributes.
class Person:
    def person_info(self,name,age):
        print("Inside Person class")
        print("Name :",name, "Age :",age)
#parant class 2
class Company:
    def Company_info(self,company_name,location):
        print("Inside Company class")
        print("Name :",company_name,"Location :",location)
# Child class
class Employee():
    def Employee_info(self,salary,skills):
        print("Inside Employee Calss")
        print("Sarary :",salary,"Skills :",skills)
#create object of employee
emply1 = Employee()
emply1.Employee_info(4564,"Software Engineering")

emply2 = Person()
emply2.person_info(4564,"Software Engineering")

emply3 = Company()
emply3.Company_info(4564,"Software Engineering")
