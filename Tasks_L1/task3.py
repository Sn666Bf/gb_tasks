# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = int(input("Введите число: "))
a = str(number)
b = str(number) * 2
c = str(number) * 3

result = int(a) + int(b) + int(c)
print(f'Сумма значений n + nn + nnn равна {result}')
