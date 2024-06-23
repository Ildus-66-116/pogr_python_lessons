my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

my_dict.update(dict(six=6))
print(my_dict)

my_dict.update(dict([('five', 5), ('two', 42)]))    # дает обновлять
print(my_dict)
print()

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)   # через | объединяются словари
print(new_dict)