my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)    # формируется новое множество находящиеся в двух множеств
print(f'{my_set = }\n{other_set = }\n{new_set = }')
print()

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set        # intersection = &
print(f'{my_set = }\n{other_set = }\n{new_set = }')
