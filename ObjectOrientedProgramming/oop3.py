class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)
print("hi".__class__)


class Garage:
    def __init__(self):
        self.cars = []
    # When you define the following 2 dunder methods you can use a for loop

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self)} cars.'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford)
for car in ford:
    print(car)
