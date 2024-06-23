data = [2, 4, 6, 8, 10, ]
print(type(data))
for item in data:
    print(item, end='\t')
print()

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')      # * перед любой последовательности это символ распаковки, короткая запись for
