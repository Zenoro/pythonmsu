"""
Чемпионы дзена

Ввести построчно список участников некоторого соревнования на скорость
неизвестно чего в виде Имя Фамилия Название команды часы:минуты:секунды (последняя строка пустая),
и вывести всех, кто занял первые три места (минимальное затраченное неизвестно на что время;
одно место может занять несколько человек, если время совпадает), в порядке возрастания времени,
а внутри одного времени — лекcикографически: фамилия, имя, команда.
Дополнительное условие: таблица чемпионов должна быть аккуратной:
поля «Имя», «Фамилия», «Название команды» и «Время» должны начинаться в одном столбце,
между ними должен быть минимум один пробел, при этом строки должны иметь минимально возможную длину.
"""
from operator import itemgetter


def timetosec(t):
    t = t.split(':')
    return (sum([60**i*int(t[-i-1]) for i in range(len(t))]))


# copy name, surn, company, time
records, name, surname, company, timestring, time = [], [], [], [], [], []
while s := input():
    if not s:
        break
    s = s.split()
    name.append(s[0])
    surname.append(s[1])
    company.append(' '.join(s[2:-1]))
    timestring.append(s[-1])
    time.append(timetosec(s[-1]))

# sort time, create good records of ALL users
lens = [max([len(i) for i in name]), max([len(i) for i in surname]), max([len(i) for i in company])]
records = [(' '.join([name[j].ljust(lens[0]), surname[j].ljust(lens[1]), company[j].ljust(lens[2]), timestring[j]]),
            time[j], surname[j], name[j], company[j]) for j in range(len(name))]

# some magic from python manual (using itemgetter)
res = sorted(records, key=itemgetter(1, 2, 3, 4))

if len(name) > 3 and len(set(time)) != 1:
    cc = 0
    counter = sorted(list(set(time)))[:3]
    for i in range(3):
        cc += time.count(counter[i])
    for i in range(cc):
        print(list(res[i])[0])
else:
    for i in range(len(name)):
        print(list(res[i])[0])
