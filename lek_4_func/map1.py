texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)       # принимает функцию и последовательность
print(*res)                                 # * распаковывает
