# Ветвление в Python
# Операция сравнения '==' проверка равентсва '>=' ...
# Зарезервированые if - если, else - еще, elif - если еще, case и match

pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешен')  # 4 пробела внутри функции
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны!')
else:
    print('Доступ запрещен')
print('Работа завершена')
