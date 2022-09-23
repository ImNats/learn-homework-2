"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""


from datetime import date, timedelta, datetime


def print_days():
    today = date.today()
    yesterday = today + timedelta(days=-1)
    long_ago = today + timedelta(days=-30)

    print('Вчера: ' + yesterday.strftime('%Y-%m-%d'))
    print('Сегодня: ' + today.strftime('%Y-%m-%d'))
    print('30 дней тому назад: ' + long_ago.strftime('%Y-%m-%d'))


def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
