def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return a


a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')  # при не изменяемых начальный аргумент не меняется

print()


def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return data


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')  # если передали изменяемый объект, то начальный после функции тоже меняется
