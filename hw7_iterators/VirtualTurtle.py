"""
Примитивная черепашка

Написать параметрическую генератор-функцию turtle(coord, direction),
описывающую движение «черепахи» по координатной плоскости.
coord — это кортеж из двух целочисленных начальных координат,
direction описывает первоначальное направление (0 — восток, 1 — север, 2 — запад, 3 — юг).
Координаты увеличиваются на северо-восток.
Генератор принимает три команды:
"f" (переход на 1 шаг вперёд),
"l" (поворот против часовой стрелки на 90°),
"r" (поворот по часовой стрелке на 90°) и возвращает текущие координаты черепахи.
"""


def turtle(coord, direction):
    buf = yield direction
    x, y = coord
    while buf:
        if buf == 'f':
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y -= 1
        elif buf == 'l':
            direction = (direction + 1) % 4
        elif buf == 'r':
            direction = (direction - 1) % 4
        buf = yield (x, y)
