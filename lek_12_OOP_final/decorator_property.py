"""Декоратор property позволяет создавать “геттеры”. Это методы, которые выдают
себя за свойства, позволяют прочитать результат, но блокируют возможность
записи."""


class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


user = User('Стивен')
print(f'{user.name = }')
user.name = 'Славик'  # AttributeError: can't set attribute 'name'
