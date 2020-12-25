# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

elements = []
element = ''

while True:
    if element != 'Q':
        element = input('Введите значение: ')
        elements.append(element)
    elif element == 'Q':
        elements.pop(len(elements) - 1)
        break

print(elements)
i = 0
for n in range(len(elements) // 2):
    elements[i], elements[i+1] = elements[i+1], elements[i]
    i += 2
print(elements)
