my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')      # изменения внеслись в оба list(ссылка на один данные), для этого нужно copy
print()
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()               # создали новую область памяти
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
