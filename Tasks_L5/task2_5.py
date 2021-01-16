# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open('task2.txt', 'r', encoding='utf-8')

i = 0
for line in file:
    items = len(line.split())
    i += 1
    print(f'В строке {i}, количество слов равно {items} ')

file.close()

file = open('task2.txt', 'r', encoding='utf-8')

lines_count = len(file.readlines())
print(f'Всего строк в файле {lines_count}')

file.close()
