"""
Функция побольше

Написать функцию maxfun(),
которая принимает переменное число параметров:
числовую последовательность S, функцию F1 и, возможно, ещё несколько функций F2 … Fn.
Возвращает она ту из функций Fi, сумма значений которой на всех элементах S наибольшая.
Если таких функций больше одной, возвращается Fi с наибольшим i.
"""


def maxfun(S, *funcs):
    summs = []
    for j in range(len(funcs)):
        summs.append(sum([funcs[j](S[i]) for i in range(len(S))]))
    maxmb = max(summs)
    return funcs[summs.index(maxmb)] if summs.count(maxmb) == 1 else funcs[summs[::-1].index(maxmb)]
