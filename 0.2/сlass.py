class Person:
    name = "Ivan"
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course=1

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

valera = Student ("Вася", 19)
valera.set("Валера", 17, 5)
print("Имя:", valera.name, ", возраст -", valera.age, ", курс - ", valera.course)


vlad = Person ("Влад",25)
# vlad.set("Влад",25)
print(vlad.name + " " + str(vlad.age))

ivan = Person ("Иван", 56)
# ivan.set("Иван", 56)
print(ivan.name)
print(ivan.age)

print(2+2)
print('2'+'2')