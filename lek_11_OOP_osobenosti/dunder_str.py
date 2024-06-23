class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):      # дандер __str__ позволяет передать в print строку
        return f'Экземпляр класса User с именем "{self.name}"'


user = User('Ildus')
user1 = User('Alex')
print(user)
print(user1)
