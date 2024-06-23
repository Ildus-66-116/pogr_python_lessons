DEFAULT = 42
num = int(input('Введите уровень или ноль для значения по умолчанию: '))
level = num or DEFAULT  # Не явно приводится к логической проверки True/False, если 0 то False = > будет DEFAULT
print(level)

name = input('Как вас зовут? ')
if name:                        # Также при пустой строке false переход на else
    print(f'Привет, {name}')
else:
    print('Ананим, приветствую')

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:                 # когда будет пусто false и выход из while
    print(data.pop())       # pop удаляет последний элемент