lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]


print(max(lst_1, default=None))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))
