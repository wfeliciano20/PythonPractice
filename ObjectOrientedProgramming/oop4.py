class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 40


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


class Bar:
    @staticmethod
    def hi():
        print('Hello I don\'t take parameters')


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(f'{rolf.name} has a salary of ${rolf.salary}')
rolf.marks.append(99)
rolf.marks.append(80)
print(f'The average of {rolf.name} in his marks is {rolf.average()}')
