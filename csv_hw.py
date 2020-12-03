# Создайте список словарей:
#         [
#         {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#         {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#         {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#     ]
# Запишите содержимое списка словарей в файл в формате csv


import csv

data = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]


with open('./data.csv', 'w', encoding='utf-8', newline='') as f:
    fields = list(set(data[0]))
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for record in data:
        writer.writerow(record)

