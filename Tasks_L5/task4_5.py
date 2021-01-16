# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',

}

with open('task4.txt', 'r', encoding='utf-8') as f:

    for i in range(1, 5):
        x = f.readline().split()

        x[0] = my_dict.get(x[0])
        test_content = (' '.join(x))
        print(test_content)
        v = open('task4_new.txt', 'a', encoding='utf-8')
        v.write(test_content + '\n')
        v.close()

