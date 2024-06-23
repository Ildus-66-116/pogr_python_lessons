data = 42
print(isinstance(data, int))    # Целое число 42 относится к int? Если да то True

data = True
print(isinstance(data, int))    # Логический тип это подкласс int

data = 3.14
print(isinstance(data, (int, float, complex)))  # Проверяет на 3 типа
