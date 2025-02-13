def my_func():
    pass  # ничего не делать


def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None

print(quadratic_equations(2, -3, -9))
