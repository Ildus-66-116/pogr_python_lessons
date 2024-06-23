# Неизменяемые:
#
# int, bool, float, complex - числа
# str, tuple, bytes - последовательности
# set - множества
#
# Изменяемые:
#
# list, bytearray - последовательности
# frozenset - множества
# dict - отображения

# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))         # не изменяет, а создает новый объект
#
# txt = 'Hello world'
# txt[5] = '_'            # не даст изменить выдаст ошибку

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')     # не изменяет, а создает новый объект
print(txt, id(txt))
