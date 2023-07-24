"""
Спиральки

Написать класс Spiral, экземпляр которого образуется из строки,
содержащей одну или несколько последовательностей одинаковых символов,
при этом одинаковые символы группируются в порядке их первого вхождения,
например Spiral("1233443213") → 11 22 3333 44.
При преобразовании в строку такая последовательность должна «закручиваться в спираль» против часовой стрелки,
начиная с направления «вправо» (см. пример).
Помимо преобразования в строку объект типа Spiral должен:
    Поддерживать сложение с таким же объектом:
        существующие в исходном объекте последовательности увеличиваются на соответствующее количество символов,
        новые — добавляются в конец
    Поддерживать вычитание объектов типа Spiral, при этом
        существующие последовательности уменьшаются в длине
        (до полного исчезновения, если в вычитаемом было не меньше таких символов)
    Поддерживать умножение на натуральное число N
        (количество символов в последовательностях увеличивается в N раз)
    Поддерживать итератор по всем символам последовательности
"""

import sys


def makeword(dd: dict) -> str:
    return "".join([i * dd[i] for i in dd])


class Spiral:
    def __init__(self, s):
        self.diction = {}
        for c in s:
            if self.diction.get(c, 0):
                self.diction[c] += 1
            else:
                self.diction[c] = 1
        self.word = makeword(self.diction)

    def __add__(self, other):
        return Spiral(self.word + other.word)

    def __mul__(self, a):
        return Spiral(self.word * a)

    def __sub__(self, other):
        temp = self.diction.copy()
        for c in temp:
            if temp[c] > 0:
                temp[c] -= other.diction.get(c, 0)
        return Spiral(makeword(temp))

    def __iter__(self):
        for i in self.word:
            yield i

    def __str__(self):
        ncells = int(1.5 * sum(self.diction.values()) ** 0.5) + 1
        xcord, ycord = ncells // 2, ncells // 2
        minc, maxc = [xcord, ycord], [xcord, ycord]
        fields = [[" " for i in range(ncells)] for k in range(ncells)]
        direction = [0, 1]
        chari, stopper = 0, 1
        for c in self.word:
            chari += 1
            fields[xcord][ycord] = c
            mycoord = [xcord, ycord]
            minc = [min(minc[i], mycoord[i]) for i in range(2)]
            maxc = [max(maxc[i], mycoord[i]) for i in range(2)]
            xcord += direction[0]
            ycord += direction[1]
            if chari == stopper:
                chari = 0
                stopper += 1
                direction = [-direction[1], direction[0]]

        res = []
        for r in fields[minc[0]:maxc[0]+1]:
            rows = "".join(r[minc[1]:]).rstrip()
            res.append(rows)
        return "\n".join(res)


exec(sys.stdin.read())
