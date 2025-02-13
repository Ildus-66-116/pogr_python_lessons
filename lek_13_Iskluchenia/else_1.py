MAX_COUNT = 5

result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили результат')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        try:
            result = 100 / num
        except ZeroDivisionError as e:
            result = float('inf')
        break

print(f'{result = }')
