"""
Много знаков Пи

https://uneex.org/LecturesCMC/PythonIntro2022/Homework_ChudnPi
"""


def PiGen():
    from decimal import Decimal, getcontext
    from math import factorial
    getcontext().prec = 9999
    summ = 0
    i = 0
    num = 426880 * Decimal(10005).sqrt()
    while 1:
        summ += Decimal((factorial(6*i) * (545140134 * i + 13591409)) /
                        Decimal((factorial(i)**3 * factorial(3*i)) * (Decimal(-262537412640768000)**i)))
        res = num / summ
        i += 1
        yield res
