"""
Без двух нулей

Написать функцию No_2Zero(N, K),
которая вычисляет количество N-значных чисел в системе счисления с основанием K,
таких что их запись не содержит двух подряд идущих нулей.
Лидирующие нули не допускаются. Для EJudge N⩽33.
"""


def No_2Zero(N, K):
    d = [0, 1]
    for i in range(1, N+1):
        d.append((d[i] + d[i-1]) * (K-1))
    return d[-1]