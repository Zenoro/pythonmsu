"""
MRO C3

Написать программу, на вход которой подаётся синтаксически верный код на ЯП Python,
состоящий только из объявления классов верхнего уровня, без пустых строк и многострочных констант.
В наследовании используются только уже определённые ранее в этом коде классы.
На выходе программа должна отчитаться, допустимо ли наследование,
которое (возможно) встретилось в коде (с точки зрения MRO C3), и вывести "Yes" или "No".
"""


def merge(name, args):
    res = [name]
    i = 0
    while i < len(args):
        if args[i] != '' and args[i] != []:
            char = args[i][0]
        else:
            i += 1
            continue
        if char == '#':
            break
        if any([k.index(char) > 0 if char in k else False for k in args]):
            i += 1
            continue
        else:
            res.append(char)
            for k, j in enumerate(args):    # механизм удаления первой буквы
                if j != [] and j[0] == char:
                    args[k].pop(0)
            i = 0
    flag = 1 if len(res) < len(args) else 0
    return (res, flag)


ff = dict()
i = 0
while s := input():
    if s.split()[0] == "class":
        if s.split("(")[0] == s:
            name = s.split()[1][:-1].strip()
            ff[name] = "#"
        else:
            name = s.split()[1].split("(")[0]
            links = [i.strip() for i in s.split("(")[1].split(":")[0][:-1].split(",")]
            ff[name] = links

if ff != {}:
    for i in ff:
        val = ff[i]
        com = []
        for j in val:
            getter = (ff.get(j, '#'))
            com.append(getter)
        if val not in com:
            com.append(val)
        d, fl = merge(i, com)
        if fl == 0:
            ff[i] = d
        else:
            print("No")
            break
    else:
        print("Yes")
else:
    print("Yes")
