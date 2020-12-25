# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print('Вариант 1')
numbers = [7, 5, 3, 3, 2]
user_number = int(input('Введите число: '))

b = numbers.append(user_number)
numbers.sort()
numbers.reverse()
print(numbers)

input('Нажмите Enter для продолжения')

print('Вариант 2')

numbers = [140, 76, 55, 33, 33, 21]
user_number = int(input('Введите число: '))


max_number = max(numbers)
min_number = min(numbers)
if user_number > max_number:
    numbers.insert(0, user_number)
elif user_number in numbers:
    numbers.insert(numbers.index(user_number), user_number)
elif user_number < min_number:
    numbers.append(user_number)
elif user_number not in numbers:
    numbers.append(user_number)
    numbers.sort()
    numbers.reverse()


print(numbers)
