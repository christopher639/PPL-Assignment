class IndustialTraining:
    def __init__(self,students,course,seats,laptops,lectures):
        self.students = students
        self.course = course
        self.seats = seats
        self.laptops = laptops
        self.lectures = lectures
    def training_info(self):
        print(f"Training  Is composed of the following \n:Number Of students :{self.students}\n Number of course :{self.course}\nNumber of seats :{self.seats}\nNumber of seats:{self.laptops}\nNumber of Lectures :{self.lectures}")
    def name_of_course(self):
        print("\nCouser Under understial training ")
        courses = {"Ajira":"CSC000","System Development":"CSC220","Security":"CSC2220","Huawei":"CSC4637"}
        for key, course in courses.items():
            print(f"Couses name: {key}:, Couse title :{course}")
        completed_course = input("Enter the couse you have completed :")
        for key, course in courses.items():
            if completed_course == key:
                print(f"The course you have completed is {course}")
            else:
                print("the course you entered is not found :")
    def student_name(self):
        names = ["Topaz","James","Karam","Jim","Nathan","Festus","Haron","Nathan","Nophothaly"]
        for name in names:
            print(f"{name } is a student in understial Training")
    def student_marks(self):
        marks = [45,50,56,35,35,43,23,234,24,24,24,54]
        for mark in marks :
            print(f"Mark{marks.index(mark)} : {mark}")




      
obj1 =  IndustialTraining(120,8,120,120,2)
obj1.training_info()
obj1.name_of_course()
obj1.name_of_course()
obj1.student_marks()

