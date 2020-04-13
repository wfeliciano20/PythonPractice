cars = {
    {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
    {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 350},
    {'make': 'Mazda', 'model': 'MX-5', 'mileage': 40000, 'fuel_consumed': 900},
    {'make': 'Mini', 'model': 'Cooper', 'mileage': 31000, 'fuel_consumed': 235}
}


def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    return mpg


def car_name(car):
    name = '{} {}'.format(car['make'], car['model'])
    return name


def print_car_info(car):
    mpg = calculate_mpg(car)
    name = car_name(car)
    print('{} does {} miles per gallon.'.format(name, mpg))


for car in cars:
    print_car_info(car)
