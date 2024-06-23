my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))   # задали 5 как значение по умолчанию
print(my_dict.get('ten', 5))    # не работает т.к. в этом ключе есть значение
print(my_dict)