class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Creating new student")

    def welcome(self):
        print("Welcome student, ", self.name)
    def get_marks(self):
        return self.marks
 

s1 = Student("Viral",80)
s1.welcome()
print("Marks: ",s1.get_marks())






