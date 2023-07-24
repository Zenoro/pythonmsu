"""
Чёт-нечет

Написать генератор-функцию seesaw(sequence),
которой на вход передаётся итерируемая целочисленная последовательность,
а конструируемый ею генератор возвращает поочерёдно то чётный,
то нечётный элемент последовательности в порядке следования.
Если элементы одного типа заканчиваются, возвращаются только элементы другого.
"""


def seesaw(seq):
    from itertools import zip_longest
    chet = []
    nechet = []
    for i in seq:
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
        res = zip_longest(chet, nechet)
    for i in res:
        for k in i:
            if k is not None:
                yield k
