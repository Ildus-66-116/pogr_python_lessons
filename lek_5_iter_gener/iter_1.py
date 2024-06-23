# Функция iter имеет формат iter(object[, sentinel]). object является обязательным
# аргументом. Если объект не реализует интерфейс итерации через методы __iter__
# или __getitem__, получим ошибку TypeError.

a = 42
#iter(a) #TypeError.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)   # второй раз не вызывается т.к. функция iter срабатывет 1 раз после вылова

