a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c                               # неизменяемое - неизменяемо!!!, создается новый объект
print(a, id(a), b, id(b), c, id(c))
