# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(dividend, divider):
    try:
        result = dividend / divider
    except ZeroDivisionError:
        return "ошибка, на 0 делить нельзя"

    return round(result, 2)


print(my_func(float(input("Введите делимое: ")), float(input("Введите делитель: "))))
