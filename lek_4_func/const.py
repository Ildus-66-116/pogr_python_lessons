LIMIT = 1_000


def func(x, y):
    result = x ** y % LIMIT     # обратились к константе из глобальной области видимости
    return result


print(func(42, 73))