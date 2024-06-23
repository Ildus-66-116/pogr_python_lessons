import os

p = 'C:/Users/Ильдус/Documents/Моя учеба/Основы Python/praktika/lek_6_moduli/'
print(p)

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')