from random import choice, randint


class Student:
    object_count = 0

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self.count_objects()

    def info(self):
        return f'{self.name} {self.age}'

    def get_name(self):
        return self._name

    def get_age(self):
        return self.get_age()

    def set_age(self, age: int):
        if age > self._age:
            self._age = age
        else:
            raise ValueError("Age cannot be decreased")  # штука для поднятия ошибок

    @property  # свойство???? надо бы загуглить
    def name(self):
        return self._name

    @staticmethod
    def count_objects():
        Student.object_count += 1


class HomelessStudent(Student):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def info(self):
        return f'{self.name} {self.age} homeless'


students = []
names = ['Ilias', 'Ruslan', 'Riia', 'Kira', 'Vlad', 'Anatoliy', 'Stepan']
n = int(input('amount of students: '))
for i in range(1, n + 1):
    name = choice(names)
    age = randint(16, 22)
    students.append(Student(name=name, age=age))

for j in students:
    print(j.info())

print(Student.object_count)

definitely_not_me = HomelessStudent(name='Ruslan', age=18)
print(definitely_not_me.info())
print(Student.object_count)
print(HomelessStudent.object_count)
