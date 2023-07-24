"""
Произвольная точность

Вводится две строки: произвольная функция над x, содержащая операции, применимые к типу decimal.Decimal,
имеющая единственный корень на интервале (-1.5, 1.5),
непрерывная на нём и принимающая значения разных знаков на концах интервала, и натуральное число D.
Вывести корень данной функции с точностью ровно D знаков после запятой (нули тоже выводятся).
Воспользоваться десятичным контекстом для задания точности (см. примеры выше на странице документации).
"""


from decimal import Decimal, localcontext, getcontext


def func(f):
    def reh(x):
        return eval(f)
    return reh


funcinput = input()
pr = int(input())
getcontext().prec = pr + 4

g = func(funcinput)
leftside, rightside, res = Decimal("-1.5"), Decimal("1.5"), 0

while Decimal(g(res)) != Decimal("0") and round(leftside, pr) != round(rightside, pr):
    res = (rightside + leftside) / Decimal("2")
    if Decimal(g(res)) > 0:
        rightside = res
        continue
    if Decimal(g(res)) < 0:
        leftside = res
        continue

with localcontext() as ct:
    ct.prec = pr
    print(f'{Decimal(res):.{pr}f}')
