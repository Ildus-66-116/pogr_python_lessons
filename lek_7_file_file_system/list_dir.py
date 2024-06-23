import os
from pathlib import Path

# print(os.listdir())
#
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)
#
# print()
# (path = os.path.join(root, name))
path = '/lek_7_file_file_system'
name_file = []
for dir_path, dir_name, file_name in os.walk(path):
    print(dir_path)
    for name in file_name:
        path_1 = os.path.join(dir_path, name)
        name_file.append(path_1)

list(map(lambda x: print(x), name_file))

my_dict = {"var1": 1, "var2": 2}
my_list = []
my_list.append(my_dict)
print(my_list)




