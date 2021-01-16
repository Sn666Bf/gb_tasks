# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# test_file = open('test.txt', 'w', encoding='utf-8')

# while True:
#     x = input('Введите любое значение. Для выхода нажмите Enter: ')
#     if x == '':
#         test_file.close()
#         break
#     else:
#         test_file.write(x)


with open('test.txt', 'w', encoding='utf-8') as f:
    while True:
        x = input('Введите любое значение. Для выхода нажмите Enter: ')
        if x == '':
            break
        else:
            f.writelines(x + '\n')

