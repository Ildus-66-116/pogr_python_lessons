""" Функция vars()
Функция без аргументов работает аналогично функции locals(). Если передать в vars
объект, функция возвращает его атрибут __dict__. А если такого атрибута нет у
объекта, вызывает ошибку TypeError.
"""

print(vars(int))
