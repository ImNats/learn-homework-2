"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


import csv


applicants_list = [
    {'name': 'Иван', 'age': 45, 'job': 'учитель'},
    {'name': 'Петр', 'age': 23, 'job': 'каскадер'},
    {'name': 'Лена', 'age': 35, 'job': 'бухгалтер'},
    {'name': 'Анна', 'age': 12, 'job': 'продавец'}
]


def main():
    #  подготовить файл к записи
    with open('applicants_list.csv', 'w', encoding='utf-8') as file_new:
        file_new.close
    with open('applicants_list.csv', 'w', encoding='utf-8', newline='') as file_new:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file_new, fieldnames=fields, delimiter=';')
        writer.writeheader()
        for applicants_list_itm in applicants_list:
            writer.writerow({
                'name': applicants_list_itm['name'],
                'age': applicants_list_itm['age'],
                'job': applicants_list_itm['job']
                })


if __name__ == "__main__":
    main()
