"""
Скрытое послание

Ввести две строки и проверить, содержится ли вторая в первой,
с учётом того, что символы второй строки могут находиться в первой
на некотором равном расстоянии друг от друга.
Вывести YES или NO.
"""


s = input()
i = input()
sbuf = ""

if i == "":
    print("YES")
elif not s or not i:
    print("NO")
elif len(i) == 1:
    if i in s:
        print("YES")
    else:
        print("NO")
else:
    while i[0] in s and i[1] in s:
        ks = s.index(i[0])
        k = s.index(i[1])
        dk = k - ks
        sbuf = s[ks::dk]
        if i in sbuf:
            print('YES')
            break
        else:
            if i[0] in s[(ks+1):]:
                s = s[(ks+1):]
            else:
                print("NO")
                break
    else:
        print("NO")
