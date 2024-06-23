def func(a):
    x = 1       # замкнули x внутри функции
    res = x + a
    return res


x = 100
print(func(5))

def add_str(a: str, b: str) -> str:
    return a + ' ' + b

print(add_str('Hello', 'world!'))