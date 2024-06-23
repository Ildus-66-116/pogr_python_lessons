data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введите число: '))
if num in data:                         # in проверяет что есть в data
    print('Леонардо придает привет!')

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введите число: '))
if num not in data:                         # not in проверяет что нет в data
    print('Леонардо грустит')
else:
    print('Леонардо придает привет!')

