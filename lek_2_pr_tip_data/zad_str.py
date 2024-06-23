text = input("Введите текст: ")
if text.isnumeric():
    num = int(text)
    print(bin(num))
    print(oct(num))
    print(hex(num))
elif text.isascii():
    print('Text in ASCII')
else:
    print('Text not ASCII')
