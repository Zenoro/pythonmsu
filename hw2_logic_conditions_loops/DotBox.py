"""
Ящик с точками

Вводить вещественные числа x, y и z по три в строке через запятую,
считая их координатами точек (не менее одной тройки).
Конец ввода — пустая строка.
Вывести минимальный объём параллелепипеда со сторонами,
параллельными осям координат, содержащего все точки.
"""


res = 1
a, b, c = eval(input())
maxim = [a, b, c]
minim = [a, b, c]

while s := input():
    if not s:
        break
    a, b, c = eval(s)
    lis = [a, b, c]
    for i in range(0, 3):
        maxim[i] = max(lis[i], maxim[i])
        minim[i] = min(lis[i], minim[i])

for i in range(0, 3):
    res *= abs(maxim[i] - minim[i])
print(res)
