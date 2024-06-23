year = int(input("Введите год yyyy: "))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:    # ленивый if если в 1 части false далее and не проверяется
    print('Обычный')
else:
    print('Високосный')
