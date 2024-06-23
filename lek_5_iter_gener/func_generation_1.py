def factorial(n):
    number = 1
    # result = []
    for i in range(1, n + 1):
        number *= i
        yield number  # превратили обычная функция в функции генератор
        # причем yield запоминает ранее сгенерированные данные
    #     result.append(number)
    # return result


for i, num in enumerate(factorial(5), start=1):
    print(f'{i}! = {num}')
