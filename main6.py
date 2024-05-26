# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main6.py
# Этот код на языке Python определяет два класса: Teacher и School.#
#  Класс Teacher имеет метод teach(),
# который печатает «Преподаватель учит» (что в переводе на русский означает «Учитель учит»).
#  Класс School имеет метод __init__(),
# который принимает в качестве аргумента объект new_teacher и присваивает его атрибуту teacher.
# У него также есть метод start_lesson(), который вызывает метод teach() объекта teacher.
#  Затем код создает объект my_teacher класса Teacher и объект my_school класса School,
# передавая my_teacher в качестве аргумента конструктору School.
#  Затем он печатает объекты my_teacher и my_school и вызывает метод start_lesson() для my_school,
# который, в свою очередь, вызывает метод teach() для my_teacher.
class Teacher():
    def teach(self):
        print("Преподаватель учит")

class School():
    def __init__(self, new_techer):
        self.teacher = new_techer

    def start_lessone(self):
        self.teacher.teach()


my_teacher = Teacher()
my_school = School(my_teacher)
print(my_teacher)
print(my_school)
my_school.start_lessone()