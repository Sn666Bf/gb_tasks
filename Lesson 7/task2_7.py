# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import abstractmethod


class Clothes:
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def material_consumption_coat(self):
        pass

    @abstractmethod
    def material_consumption_suit(self):
        pass


class Coat(Clothes):

    @property
    def material_consumption_coat(self):
        return round((self.parameter / 6) + 0.5)


class Suit(Clothes):

    @property
    def material_consumption_suit(self):
        return round(2 * self.parameter + 0.3)


coat = Coat(int(input('Введите размер пальто: ')))
suit = Suit(int(input('Введите рост: ')))

summ_material = float(coat.material_consumption_coat) + float(suit.material_consumption_suit)


print(f'расход ткани на пальто составляет: {coat.material_consumption_coat}')
print(f'расход ткани на костюм составляет: {suit.material_consumption_suit}')
print(f'общий расход ткани составляет: {summ_material}')
