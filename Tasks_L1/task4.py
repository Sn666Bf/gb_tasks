# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = []

numbers = int(input('Введите целое положительное число: '))
numbers = str(numbers)

for number in numbers:
    a.append(number)
# print(max(a))

i = 0
max_number = '0'


while i < len(a):
    for number in a:
        if number > max_number:
            max_number = number
    i += 1
print(max_number)
