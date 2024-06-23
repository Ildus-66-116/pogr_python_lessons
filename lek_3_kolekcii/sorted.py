# my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]   # сортировать разного типа не возможно
# my_list.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
# res = sorted(my_list) # TypeError: '<' not supported between instances of 'int' and 'str'

# Функция sorted
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)         # по умолчанию сортировка по возрастанию
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)    # сортировка по убыванию
print(my_list, rev_list, sep='\n')
print()

# метод sort
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

