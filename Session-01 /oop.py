class Student:

    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")

    def study(self):
        print(f"{self.name} is studying.")


student1 = Student("Ali", 123, "AI")
student2 = Student("Sara", 456, "Computer")


student1.introduce()
student1.study()

print("----------------")

student2.introduce()
student2.study()
