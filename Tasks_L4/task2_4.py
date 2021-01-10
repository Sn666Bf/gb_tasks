# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

numbers = []
number = 0
new_numbers = []

randint_maximum = int(input('Введите максимальное значение рандомайзера: '))
iterations = int(input('Введите количество значений в списке: '))
i = 0

# while i != iterations:
#     number = random.randint(1, randint_maximum)
#     numbers.append(number)
#     i += 1
# print(numbers)

for el in range(iterations):
    number = random.randint(1, randint_maximum)
    numbers.append(number)

for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        new_numbers.append(numbers[i + 1])
print(new_numbers)

