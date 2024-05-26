#am developing the whole univerty and class with object
#to learn and practice more on python
class University:
    def __init__(self,name,capacity,location):
        self.name = name
        self.capacity = capacity
        self.location = location
    #method to print university information
    def uni_info(self):
        print(f"{self.name} is located in {self.location} with {self.capacity} number of students")
    #method to calculate area caverd  my premised
    def area_of_premises(self,length,width):
        self.length =length 
        self.width = width
        area = length * width
        area_info = f" The area of {self.name} is {area} m squared"
        return area_info
    #method to print couses offered at university
    def course_offerd(self):
        #using list to print cousrse offered
        courses = ["Computer Science","Information technology"," Bachelor of Commmerce","Cyber security"]
        print(f"{self.name} offers the couses :")
        for course in courses :
          print(f"{self.name} offers : {course}")
    def stud_feedback(self):
        name = input(f"Enter Your name as student in {self.name} :")
        course = input(f"Enter Course parsuing at {self.name}:")
        feedback = input(f"Give feedback about {self.name} :")
        message  = f"{name} taking {course} says that {feedback}"
        return message

    
    #is univers
#let creat instance of the class the the objects
obj1 = University("Kibabii University", 2000,"Bungoma")
print(obj1.uni_info())
print(obj1.area_of_premises(300,200))
print(obj1.course_offerd())
print(obj1.stud_feedback())
