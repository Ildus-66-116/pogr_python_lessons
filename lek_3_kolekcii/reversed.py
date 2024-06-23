# функция reversed
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)

rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)

# метод reverse
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)
print()

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1]            # тоже разворот [start:stop:step]
print(my_list, new_list, sep='\n')
