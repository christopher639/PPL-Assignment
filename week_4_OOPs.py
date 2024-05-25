#This is Power lear week four assignment
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    #method to print and introduce the person
    def person_intro(self):
        print(f"My name is: {self.name} an {self.age} years old and am {self.gender} ")
#Instance of a person class
personx = Person("Christopher Bundi",22,"MALE")
print(personx.person_intro())
#OUTPUT
#My name is: Christopher Bundi an 22 years old and am MALE 
#Great am learning python well
