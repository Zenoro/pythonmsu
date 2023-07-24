"""
Точная дробь.

Вводится строка, содержащая вычислимое арифметическое выражение.
Выражение может содержать пять арифметических операций (+ - / * %), скобки, вещественные числа и пробелы.
Вычислить точное значение в виде натуральной дроби и вывести его.
Для представления чисел использовать тип fractions.Fraction.
"""


import re
from fractions import Fraction

s = input()
reg = re.compile(r"(\d+[\/\d.]\d+[.]*|[.]*\d+[.]*)")
s = reg.split(s)

res, ind = list(), int()
for y in s:
    if reg.match(y) is not None:
        res.append(f"Fraction('{s[ind]}')")
    else:
        res.append(s[ind])
    ind += 1

res = "".join(res)
print(eval(res))
