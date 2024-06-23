my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for tuple_data in my_dict.items():  # плохо
    print(tuple_data)

for key, value in my_dict.items():  # хорошо
    print(key, value)
    print(f'{key = } value before 100 - {100 - value}')
