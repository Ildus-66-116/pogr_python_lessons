link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')      # разбивает на элементы по /
print(urls)
a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()
