last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())         # обрезает с точки курсора


size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))
