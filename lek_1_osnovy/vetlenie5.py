year = int(input("Введите год yyyy: "))
if year % 4 != 0:   # '%' остаток от деления
    print('Обычный')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Високосный')