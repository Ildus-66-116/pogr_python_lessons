# Анонимная функция lambda
# ✔ lambda parameters: action
# Анонимные функции, они же лямбда функции — синтаксический сахар для
# обычных питоновских функций с рядом ограничений. Они позволяют задать
# функцию в одну строку кода без использования других ключевых слов.

def add_two_def(a, b):
    return a + b


add_two_lambda = lambda a, b: a + b     # одно и тоже с 7 и 8 строкой, но так делать не стоит

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))


my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])   # ключ и значение на втором х значит по значению
print(f'{s_key = }\n{s_value = }')

