"""
Арифметика функций

Написать четыре функции (функционала): ADD(f, g), SUB(f, g), MUL(f, g) и DIV(f, g),
параметрами которых могут быть как обычные объекты, так и функции от одной переменной
(проверить, является ли объект функцией можно с помощью callable(объект)).
Возвращать эти функционалы должны функцию от одной переменной h(x),
которая выполняет соответствующее действие — f(x)+g(x), f(x)-g(x), f(x)*g(x)
или f(x)/g(x) — над этими переменными.
Если f или g не были функцией, вместо f(x) используется f,
а вместо g(x) — g (например, при умножении функции на константу).
"""


def ADD(f, g):
    def func(x):
        if callable(f) and callable(g):
            return f(x)+g(x)
        elif not (callable(f) or callable(g)):
            return f+g
        else:
            return f(x)+g if callable(f) and not callable(g) else f+g(x)
    return func


def MUL(f, g):
    def func(x):
        if callable(f) and callable(g):
            return f(x)*g(x)
        elif not (callable(f) or callable(g)):
            return f*g
        else:
            return f(x)*g if callable(f) and not callable(g) else f*g(x)
    return func


def SUB(f, g):
    def func(x):
        if callable(f) and callable(g):
            return f(x)-g(x)
        elif not (callable(f) or callable(g)):
            return f-g-x
        else:
            return f(x)-g if callable(f) and not callable(g) else f-g(x)
    return func


def DIV(f, g):
    def func(x):
        if callable(f) and callable(g):
            return f(x)/g(x)
        elif not (callable(f) or callable(g)):
            return f/g
        else:
            return f(x)/g if callable(f) and not callable(g) else f/g(x)
    return func
