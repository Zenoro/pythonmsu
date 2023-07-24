"""
Фиксированная точность
Написать функцию-параметрический декоратор fix(n),
с помощью которой все вещественные (как позиционные, так и именные)
параметры произвольной декорируемой функции, а также её возвращаемое значение,
округляются до n-го знака после запятой.
Если какие-то параметры функции оказались не вещественными,
или не вещественно возвращаемое значение, эти объекты не меняются.
"""


def fix(n):
    def decorator(fun):
        def newfun(*args, **kwargs):
            temp = list(args)
            if any([type(i) == str for i in temp]):
                k = fun(*args, **kwargs)
            else:
                newargs = [round(rog, n) for rog in temp]
                k = fun(*newargs, **kwargs)
            return round(k, n) if not type(k) == str else k
        return newfun
    return decorator
