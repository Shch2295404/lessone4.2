class Teacher():
    def teach(self):
        print("Преподаватель учит")

class School( ):
    def __init__(self, new_techer):
        self.teacher = new_techer

    def start_lessone(self):
        self.teacher.teach()


my_teacher = Teacher()
my_school = School(my_teacher)
print(my_teacher)
print(my_school)
my_school.start_lessone()