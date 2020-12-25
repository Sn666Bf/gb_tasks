# *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

global_name = []
global_price = []
global_quantity = []
global_item = []


general_store = []
letter = ''

while True:
    letter = input('Введите N для начала ввода накладных, A для анализа данных или Q для выхода: ')
    if letter == 'Q':
        print('Программа будет отключена!')
        break
    elif letter == 'N':
        i = 0
        goods = int(input('Какое количество товаров указано в накладной?: '))
        while i != goods:
            i += 1
            print(f'\nТовар № {i}\n')
            
            goods_list = dict({'название': input('Введите название продукции: '),
                               'цена': input('Введите цену продукта: '),
                               'количество': input('Введите количество продукта: '),
                               'ед': input('Введите единицы измерения: ')
                               })

            general_store.append((i, goods_list))

            global_name.append(goods_list.get('название'))
            global_price.append(goods_list.get('цена'))
            global_quantity.append(goods_list.get('количество'))
            global_item.append(goods_list.get('ед'))

        print(f'\nИтого в накладной: \n{general_store}')

    elif letter == 'A':
        print(f'Название: {global_name}, \nЦена: {global_price} \nколичество: {global_quantity} \nед: {global_item}')
