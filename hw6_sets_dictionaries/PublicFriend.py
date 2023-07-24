"""
Знаком со всеми

Вводятся в столбик пары натуральных чисел через запятую.
Каждая пара M, N обозначает взаимное знакомство людей под номерами M и N.
Ввод заканчивается парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с человеком N ;) ).
Вывести через пробел в порядке возрастания номера тех, кто знаком со всеми остальными,
или пустую строку, если таких нет.
"""


buf = []

# input
x, y = eval(input())
while x != 0 or y != 0:
    buf.append((x, y))
    x, y = eval(input())
buf = sorted(list(set(buf)))
buf.append((0, 0))

# making links
res, intbuf = [], []
for i in range(1, len(buf)):
    intbuf.append(buf[i-1][1])
    if buf[i][0] != buf[i-1][0]:
        res.append((buf[i-1][0], intbuf))
        intbuf = []

# interconnect
res = dict(res)
for i in res:
    some = res.get(i)
    for j in range(len(some)):
        if i not in res[some[j]]:
            res[some[j]].append(i)

print(*[i for i in res if len(res[i]) == len(res.keys()) - 1])
