# Реализовать программу работы с органическими клетками.

# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток. (__add__())
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. (__sub__())
# Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение. (__mul__())
# Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление. (__truediv__()
# Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return str(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return str(self.quantity - other.quantity)
        else:
            return "Извините, но размер клетки не может быть отрицательным"

    def __mul__(self, other):
        return str(self.quantity * other.quantity)

    def __truediv__(self, other):
        return str(self.quantity / other.quantity)

    def visual(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.quantity // rows)]) + '\n' + '*' * (self.quantity % rows)


first_cell = Cell(int(input('Введите размер первой клетки: ')))
second_cell = Cell(int(input('Введите размер второй клетки: ')))


print(f'В первой пробирке у нас: {first_cell.quantity} клеток')
print(first_cell.visual(5))
print(f'Во второй пробирке у нас: {second_cell.quantity} клеток')
print(second_cell.visual(5))

action = int(input('Введите число от 1 до 4. 1 для сложения, 2 для вычитания, 3 для умножения, 4 для деления клеток: '))
if action == 1:
    print('Складываем клетки')
    print(first_cell + second_cell)

elif action == 2:
    print('Вычитаем клетки')
    print(first_cell - second_cell)
elif action == 3:
    print('Умножаем клетки')
    print(first_cell * second_cell)
elif action == 4:
    print('Делим клетки')
    print(first_cell / second_cell)
else:
    print('Эксперимент провален из за криворукости лаборанта! (((')
