my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)              # из первого множества удаляются элементы 2-го множества
print(f'{my_set = }\n{other_set = }\n{new_set = }')
print()
new_set_2 = my_set - other_set                      # то же самое
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
