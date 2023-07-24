"""
Подсчёт кратных

Написать функцию moar(a, b, n) от трёх параметров — целочисленных последовательностей a и b, и натурального числа n.
Функция возвращает True, если в a больше чисел, кратных n, чем в b, и False в противном случае.
"""


def moar(a, b, c):
    def counting(d):
        return sum([d[i] % c == 0 for i in range(len(d))])
    return counting(a) > counting(b)
