"""
Случилась бНОПНЯ

Текст процедуры на языке Рапира в кодировке koi8-r был несколько раз перекодирован,
причём перекодировщику сообщали совершенно произвольную исходную и целевую однобайтную кодировку
(например, из cp866 в latin_1).
Результат перекодировали из последней целевой кодировки в UTF-8.
Восстановить предполагаемый текст процедуры.
Синтаксис внутри процедуры не соблюдается, но все буквы — заглавные русские перед "ПРОЦ" и после "КНЦ;"
ничего не стоит внутри процедуры есть оператор "ВЫВОД: "
Список допустимых кодировок:
cp037 cp1006 cp1250 cp1251 cp1253 cp1254 cp1255 cp1256 cp1257 cp1258 cp437 cp720 cp737 cp775 cp850
cp852 cp855 cp864 cp866 cp869 cp874 cp875 hp_roman8 iso8859_10 iso8859_16 iso8859_4 iso8859_5
koi8_r latin_1 mac_croatian mac_greek mac_iceland mac_latin2
Максимальное количество перекодирований — 3
Известно, что в процессе перекодирования не возникало ошибок
"""


from sys import stdin


def dectokoi8(text):
    return text.decode('koi8-r')


def output(s, enc):
    kk = len(enc)
    match kk:
        case 1:
            print(dectokoi8(s.encode(enc[0])))
        case 3:
            print(dectokoi8(s.encode(enc[0].decode(enc[1]).encode(enc[2]))))
        case 5:
            print(dectokoi8(s.encode(enc[0]).decode(enc[1]).encode(enc[2]).decode(enc[3]).encode(enc[4])))


codecs = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254',
          'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737',
          'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874',
          'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5',
          'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']
enc = "!\"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ".encode("koi8-r")

s = stdin.read().rstrip()
entend = s[0:4] + s[len(s)-4:]
if '×{´F' in entend or 'KM' in entend:
    s = s.split('%')
else:
    s = s.split('\n')

# 1st encoding
pairs1 = {}
for cp1 in codecs:
    for cp2 in codecs:
        if cp1 != cp2:
            try:
                val = enc.decode(cp1).encode(cp2)
                pairs1[(cp1, cp2)] = val
                if entend.encode(cp1).decode('koi8-r') == 'ПРОЦКНЦ;':
                    for subs in s:
                        output(subs, [cp1])
                    raise SystemExit
            except SystemExit:
                quit()
            except:
                pass

# 2nd encoding
pairs2 = {}
for (cpp1, cpp2), var in pairs1.items():
    for cp1 in codecs:
        for cp2 in codecs:
            if cp1 != cp2 and cpp1 != cp1:
                try:
                    val = var.decode(cp1).encode(cp2)
                    pairs2[((cp2, cp1, cpp2, cpp1))] = val
                    if dectokoi8(entend.encode(cp1).decode(cpp2).encode(cpp1)) == 'ПРОЦКНЦ;':
                        for subs in s:
                            output(subs, [cp1, cpp2, cpp1])
                        raise SystemExit
                except SystemExit:
                    quit()
                except:
                    pass

# 3rd encodings
for (cpp1, cpp2, cpp3, cpp4), var in pairs2.items():
    for cp1 in codecs:
        for cp2 in codecs:
            if cp1 != cp2 and cpp1 != cp1:
                try:
                    val = var.decode(cp1).encode(cp2)
                    if dectokoi8(entend.encode(cp1).decode(cpp1).encode(cpp2).decode(cpp3).encode(cpp4)) == 'ПРОЦКНЦ;':
                        for subs in s:
                            output(subs, [cp1, cpp1, cpp2, cpp3, cpp4])
                        raise SystemExit
                except SystemExit:
                    quit()
                except:
                    pass
