class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)


a = Vector(2, 4)
print(a.x) # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')

