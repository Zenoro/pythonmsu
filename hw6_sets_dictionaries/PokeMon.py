"""
Покемоны

Участники некоторой карточной игры владеют несколькими колодами,
из которых они составляют свой уникальный игровой набор.
Каждая колода имеет номер; колоды с одинаковыми номерами содержат совпадающие наборы карт.
Ввести строки вида "имя игрока / номер колоды" (колода принадлежит игроку) или "номер колоды / название карты"
(карта входит в колоду); последняя строка пустая.
Вывести в алфавитном порядке имена игроков, которые могут составить игровой набор из наибольшего числа различных карт.
"""


def dictappend(d, key1, key1value2):
    if key1 not in d:
        d[key1] = [key1value2]
    else:
        d[key1].append(key1value2)
    return d


buf, dictcard, dictplayers = [], {}, {}
while s := input():
    s = s.split(" / ")
    if s[0].isnumeric():    # cards
        dictappend(dictcard, int(s[0]), s[1])
    else:
        dictappend(dictplayers, s[0], int(s[1]))

for i in dictplayers:
    for j in dictplayers[i]:
        buf += dictcard[j]
    dictplayers[i] = len(set(buf))
    buf = []
print(*sorted([ll for ll in dictplayers.keys() if dictplayers[ll] == max(dictplayers.values())]), sep="\n")
