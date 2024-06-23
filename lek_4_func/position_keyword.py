# Косая черта / и звёздочка * разделяют позиционные и ключевые параметры

def func(positional_only, /, positional_or_keyword, *, keyword_only):
    pass

print('Пример только позиционной функции:')
def pos_only_arg(arg, /):
    print(arg)


pos_only_arg(42)
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got somepositional-only arguments passed as keyword arguments: 'arg'

print('Пример только ключевой функции:')

def kwd_only_arg(*, arg):
    print(arg)


# kwd_only_arg(42)
kwd_only_arg(arg=42)

print('Пример функции со всеми вариантами параметров:')

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3) # TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'