"""
Разбор пакета

На вход подаётся содержимое некоторого пакета данных — строка в формате base85.
Пакет состоит из заголовка и тела. Заголовок содержит последовательность ненулевых байтов,
заканчивающуюся нулевым. Каждый байт заголовка — число 1, -1, 2, -2, 4, -4, 8 или -8 (других нет).
Модуль этого числа описывает количество байтов в очередном поле записи.
Тело состоит из нуля или более записей, определяемых в заголовке.
Если число отрицательное, соответствующее поле — целое со знаком, если положительное — беззнаковое.
Выравнивания между полями и между записями нет. Порядок байтов — «сетевой» (big endian).
Вывести сумму всех полей пакета.
"""


def convert(x: int, leng: int) -> int:
    if x >= 1 << (8 * leng-1):
        x -= (1 << (8 * leng - 1)) * 2
    return x


s = __import__('base64').b85decode(input().encode())

# read header
cifri = []
for i, k in enumerate(s):
    if k != 0:
        cifri.append(convert(k, 1))
    else:
        break

# prepare for battle
lenofmessage = sum([abs(i) for i in cifri])
s = s[i+1:]
packets = [s[(i-1)*lenofmessage:(i)*lenofmessage] for i in range(1, len(s)//lenofmessage + 1)]

# main()
res, testbuf = 0, []
for i in packets:
    for j in cifri:
        buf = ""
        for k in i[:abs(j)]:
            buf += bin(k)[2:].zfill(8)
        buf = int(buf, 2)
        if j > 0:   # or buf == convert(buf, abs(j)):
            res += buf
        else:
            res += convert(buf, abs(j))
        i = i[abs(j):]
print(res)
