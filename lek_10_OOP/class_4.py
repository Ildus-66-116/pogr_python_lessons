class Person:
    max_up = 3


p1 = Person()
p2 = Person()
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

p1.max_up = 12
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

Person.max_up = 42                                              # Заменили атрибут у самого класса
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')    # у p1 было имения объята, не взял у класса
