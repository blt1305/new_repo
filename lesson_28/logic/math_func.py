def calculate(a, b):
    index = 2 if a > 0 else 2.3
    return a * index / b + 4


def calculate_formula(a, b, c):
    return calculate(a, b) + calculate(a, c) + calculate(b, c) + calculate(b, a) + calculate(c, a) + calculate(c, b)
