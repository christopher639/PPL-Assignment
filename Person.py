class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastName = lname
    
    def print_name(self):
        print(self.firstname,self.lastName)

class student(Person):
    def __init__(self,fname,lname,year):
        Person.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome,",self.firstname,self.lastName,"To my Graduation ceromory in ",self.graduation_year)




x = Person("Chris","dancan")
print(x.lastName)
print(x.firstname)
x = student("Bundi Chistopher"," and  Sharon kawira",2026)
print(x.firstname)
print(x.lastName)
print(f"The graduation year is :{x.graduation_year}")
print(x.welcome())
