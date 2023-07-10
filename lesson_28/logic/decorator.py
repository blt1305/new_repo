

def multiplier(func):
    def wrapper(a, b):
        result = func(a, b)
        return result * 10
    return wrapper


@multiplier
def calculate(a, b):
    return (a + b) * 2
