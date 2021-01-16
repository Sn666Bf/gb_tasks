# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

poor_workers = []
all_bounds = []
sum_all_bounds = 0

with open('task3.txt', encoding='utf-8') as file:

    for line in file:
        new_lines = line.split()
        all_bounds.append(new_lines[1])

        if new_lines[1] < '20000':
            poor_workers.append(new_lines[0])

    for i in all_bounds:
        sum_all_bounds = sum_all_bounds + int(i)


print('Сотрудники с зарплатой ниже 20000 рублей: ', ', '.join(poor_workers))
print('средняя зарплата на всю компанию: ', sum_all_bounds / len(all_bounds) + 1)

