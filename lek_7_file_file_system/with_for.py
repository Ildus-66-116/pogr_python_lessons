with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])                            # исключаем перенос строки
        print(line.replace('\n', ''))
