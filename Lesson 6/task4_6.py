# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала!')

    def stop(self):
        print(f'машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'машина {self.name} в направлении {direction}!')

    def car_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')


class TownCar(Car):
    def car_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')
        if self.speed > 60:
            print(f'Осторожно, скорость {self.speed} для {self.name} считается превышенной!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def car_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')
        if self.speed > 40:
            print(f'Осторожно, скорость {self.speed} для {self.name} считается превышенной!!!')


class PoliceCar(Car):
    pass


# speed, color, name, is_police (булево)
town_car = TownCar(60, 'красный', 'Запорожец', False)
sport_car = SportCar(260, 'коричневый', 'Феррари', False)
work_car = WorkCar(200, 'синий', 'Трактор', False)
police_car = PoliceCar(100, 'белый', 'Форд', True)

sport_car.car_speed()
town_car.car_speed()
work_car.car_speed()
police_car.car_speed()
police_car.turn('Вправо')

print(sport_car.name)
print(town_car.is_police)

work_car.stop()
