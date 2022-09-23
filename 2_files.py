"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    #  подготовить файл к записи
    with open('referat2.txt', 'w', encoding='utf-8') as file_new:
        file_new.close

    with open('referat.txt', 'r', encoding='utf-8') as file_main:
        line_count = 0
        word_count = 0
        for line in file_main:
            line_count += 1
            word_count += len(line.split())

            new_line = line.replace(".", "!")
            with open('referat2.txt', 'a', encoding='utf-8') as file_new:
                file_new.write(f'{new_line}')

    print(f'Количество строк в файле: {line_count}')
    print(f'Количество слов в файле: {word_count}')


if __name__ == "__main__":
    main()
