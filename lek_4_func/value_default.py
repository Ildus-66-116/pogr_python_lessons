def quadratic_equations(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


print(quadratic_equations(2, -4))

print('Изменяемый объект как значение по умолчанию')


def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')

other_list = from_one_to_n(7)
print(f'{other_list = }')

print('Как правильно сделать')


def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')

other_list = from_one_to_n(7)
print(f'{other_list = }')
