"""
Фиксированная точка

Написать метакласс fixed с параметром ndigits (по умолчанию 3),
в котором все возвращаемые обычными (не статическими и не методами класса)
методами значения округляются с помощью round() до ndigits знаков после запятой,
если они вещественные по определению модуля numbers.
"""


import types
import numbers
from sys import stdin


def wrap(f, n):
    def ff(*args):
        if all([isinstance(q, numbers.Real) for q in args[1:]]):
            try:
                res = round(f(*args), n)
            except:
                res = f(*args)
        else:
            res = f(*args)
        return res
    return ff


class fixed(type):

    def __new__(metacls, future_name, future_parents, namespace, **kwds):
        roundkoef = 3
        if 'ndigits' in kwds:
            roundkoef = kwds['ndigits']
        for k in namespace:
            if isinstance(namespace[k], types.FunctionType):
                namespace[k] = wrap(namespace[k], roundkoef)
        return super().__new__(metacls, future_name, future_parents, namespace)


exec(stdin.read())
