# У неизменяемого объекта hash вычисляется, у изменяемого нет!
x = 42
y = 'text'
z = 3.14
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list))        # Получим ошибку т.к. list изменяемый
