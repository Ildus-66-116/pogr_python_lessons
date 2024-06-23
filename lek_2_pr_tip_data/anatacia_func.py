def my_func(data: list[int | float]) -> float:  # функция принимает data, анатация сообщаем, что будут принимать
    res = sum(data) / len(data)                 # данные int или float -> возвращает float
    return res


print(my_func([2, 5.5, 15, 8, 13.74]))
