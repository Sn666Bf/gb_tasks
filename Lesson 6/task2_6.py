# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина),
# width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def my_func(self):
        mass = input()
        z = input()
        return self._width * self._lenght * int(mass) * int(z)


road = Road(int(input()), int(input()))

print(road.my_func())






