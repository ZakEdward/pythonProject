# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
chet = 0

lamps_quantity = 0
lamps_price = 0
table_quantity = 0
table_price = 0
chair_quantity = 0
chair_price = 0
sofa_quantity = 0
sofa_price = 0
per = {}
for tov in goods.items():
    key, prm = tov[0], tov[1]
    per.setdefault(key)
    if prm == list(store.keys())[chet]:
        for i in store[prm]:
            lamps_quantity += i['quantity'] * i['price']
            lamps_price += i['quantity']
            per[key] = lamps_quantity
    elif prm == list(store.keys())[chet+1]:
        for i in store[prm]:
            table_quantity += i['quantity'] * i['price']
            table_price += i['quantity']
            per[key] = table_quantity
    elif prm == list(store.keys())[chet+2]:
        for i in store[prm]:
            sofa_quantity += i['quantity'] * i['price']
            sofa_price += i['quantity']
            per[key] = sofa_quantity
    elif prm == list(store.keys())[chet+3]:
        for i in store[prm]:
            chair_quantity += i['quantity'] * i['price']
            chair_price += i['quantity']
            per[key] = chair_quantity
    else:
        print(tov[0])
        chet += 1
# print(lamps_quantity, lamps_price)
# print(table_quantity, table_price)
# print(chair_quantity, chair_price)
# print(sofa_quantity, sofa_price, 'диван')
# print(per)

# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб
print('Лампа -', lamps_price, 'шт, стоимостью', lamps_quantity, 'руб')
print('Стол -', table_price, 'шт, стоимостью', table_quantity, 'руб')
print('Диван -', sofa_price, 'шт, стоимостью', sofa_quantity, 'руб')
print('Стул -', chair_price, 'шт, стоимостью', chair_quantity, 'руб')