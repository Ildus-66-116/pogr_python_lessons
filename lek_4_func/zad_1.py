def func(a=0.0, /, b=0.0, *, c=0.0):    # b не используется
    """func(a=0.0: int | float, /, b=0.0: int | float, *, c=0.0: int | float) -> : int | float"""
    # дублирует так делать не надо, надо описание действий
    if a > c:
        return a
    if a < c:
        return c
    return


print(func(c=1, b=2, a=3))  # a позиционная переменная, должна стоят 1-ой и только число
