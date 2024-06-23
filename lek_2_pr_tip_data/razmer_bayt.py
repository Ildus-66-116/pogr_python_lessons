import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)      # sys.getsizeof возвращает размер в байтах
    num *= STEP
a = 7_901_123_456_789   # позволяет _ удобно записывать большие числа
print(a)