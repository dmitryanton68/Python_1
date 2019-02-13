# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, speed, color, name, direction, is_police=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed != 0:
            return f'{self.color} TownCar {self.name} is moving'
        else:
            return f'{self.color} TownCar {self.name} is not moving'

    def stop(self):
        if self.speed == 0:
            return f'{self.color} TownCar {self.name} stops'
        else:
            return f'{self.color} TownCar {self.name} do not stop'

    def turn(self):
        if self.direction == 'right':
            return f'{self.color} TownCar {self.name} is turning to the right side'
        elif self.direction == 'left':
            return f'{self.color} TownCar {self.name} is turning to the left side'
        else:
            return f'{self.color} TownCar {self.name} is not turning'


class SportCar:
    def __init__(self, speed, color, name, direction, is_police=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed != 0:
            return f'{self.color} SportCar {self.name} is moving'
        else:
            return f'{self.color} SportCar {self.name} is not moving'

    def stop(self):
        if self.speed == 0:
            return f'{self.color} SportCar {self.name} stops'
        else:
            return f'{self.color} SportCar {self.name} do not stop'

    def turn(self):
        if self.direction == 'right':
            return f'{self.color} SportCar {self.name} is turning to the right side'
        elif self.direction == 'left':
            return f'{self.color} SportCar {self.name} is turning to the left side'
        else:
            return f'{self.color} SportCar {self.name} is not turning'


class WorkCar:
    def __init__(self, speed, color, name, direction, is_police=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed != 0:
            return f'{self.color} WorkCar {self.name} is moving'
        else:
            return f'{self.color} WorkCar {self.name} is not moving'

    def stop(self):
        if self.speed == 0:
            return f'{self.color} WorkCar {self.name} stops'
        else:
            return f'{self.color} WorkCar {self.name} do not stop'

    def turn(self):
        if self.direction == 'right':
            return f'{self.color} WorkCar {self.name} is turning to the right side'
        elif self.direction == 'left':
            return f'{self.color} WorkCar {self.name} is turning to the left side'
        else:
            return f'{self.color} WorkCar {self.name} is not turning'


class PoliceCar:
    def __init__(self, speed, color, name, direction, is_police=1):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed != 0:
            return f'{self.color} PoliceCar {self.name} is moving'
        else:
            return f'{self.color} PoliceCar {self.name} is not moving'

    def stop(self):
        if self.speed == 0:
            return f'{self.color} PoliceCar {self.name} stops'
        else:
            return f'{self.color} PoliceCar {self.name} do not stop'

    def turn(self):
        if self.direction == 'right':
            return f'{self.color} PoliceCar {self.name} is turning to the right side'
        elif self.direction == 'left':
            return f'{self.color} PoliceCar {self.name} is turning to the left side'
        else:
            return f'{self.color} PoliceCar {self.name} is not turning'


a = PoliceCar(10, 'White', 'Nissan', 'left', 1).go()
b = WorkCar(-2, 'Red', 'КАМАЗ', 'left', 1).turn()
c = TownCar(0, 'Black', 'Ford', 'left', 1).stop()
print(a, b, c, sep='\n')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, direction, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed != 0:
            return f'{self.color} {self.name} Car is moving'
        else:
            return f'{self.color} {self.name} Car is not moving'

    def stop(self):
        if self.speed == 0:
            return f'{self.color} {self.name} Car stops'
        else:
            return f'{self.color} {self.name} Car do not stop'

    def turn(self):
        if self.direction == 'right':
            return f'{self.color} {self.name} Car is turning to the right side'
        elif self.direction == 'left':
            return f'{self.color} {self.name} Car is turning to the left side'
        else:
            return f'{self.color} {self.name} Car is not turning'


class SpecialCar(Car):
    def __init__(self, speed, color, name, direction, car_type, is_police):
        Car.__init__(self, speed, color, name, direction, is_police)
        dct = {1: 'Town', 2: 'Sport', 3: 'Work', 4: 'Police'}
        self.car_type = dct[car_type]
        if self.is_police == 1 and car_type != 4:
            self.car_type = f"Special Police {dct[car_type]}"
        elif self.is_police == 1 and car_type == 4:
            self.car_type = dct[car_type]
        self.name = f'{self.name} {self.car_type}'


a = SpecialCar(10, 'White', 'Nissan', 'left', 4, 1).go()
b = SpecialCar(-2, 'Red', 'КАМАЗ', 'left', 3, 1).turn()
c = SpecialCar(0, 'Black', 'Ford', 'left', 1, 0).stop()
print(a, b, c, sep='\n')
