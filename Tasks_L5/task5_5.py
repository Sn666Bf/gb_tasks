# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

sum_numbers = 0

with open('task5.txt', 'w', encoding='utf-8') as f:
    numbers = input('Введите числа через пробел: ')
    print(f'вы ввели следующие цифры: {numbers}')
    f.write(numbers)


with open('task5.txt', 'r', encoding='utf-8') as f:
    for number in numbers.split():
        sum_numbers = sum_numbers + int(number)

print('сумма цифр равна {}'.format(sum_numbers))




