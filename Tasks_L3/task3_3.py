# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def sum_of_num():
    sum_numbers = []
    i = 0
    for i in range(3):
        i = int(input("Введите число: "))
        sum_numbers.append(i)

        sum_numbers = sorted(sum_numbers)
    return sum_numbers[1] + sum_numbers[2]


print(sum_of_num())