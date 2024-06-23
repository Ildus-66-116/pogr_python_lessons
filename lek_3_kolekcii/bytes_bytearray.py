text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
print()


x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')          # не изменяемая последовательно
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')      # изменяемая последовательность
print(f'{x = }\n{y = }')
