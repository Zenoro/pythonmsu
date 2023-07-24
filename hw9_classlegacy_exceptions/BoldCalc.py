"""
Надёжный калькулятор

https://uneex.org/LecturesCMC/PythonIntro2022/Homework_BoldCalc
"""


import re


G = globals()
PREF = "P_"


def f(s):
    if not s.startswith("#"):
        if re.search(r"(?:\b\d+[A-Za-z_])|(?:\.)|(?:\*\*)|(?://)|(?:\w\()", s):
            return "Syntax error"
        *left, right = s.replace('/', '//').split('=')
        if len(left) > 1:
            return "Syntax error"
        elif left and not left[0].isidentifier():
            return "Assignment error"
        else:
            try:
                s = re.sub(r"([A-Za-z_]\w*)", rf"{PREF}\1", right)
                res = eval(s, G)
            except NameError:
                return 'Name error'
            except:
                return "Runtime error"
            if left:
                name = PREF + left[0]
                G[name] = res
            else:
                return res


while s := input().replace(" ", ""):
    k = f(s)
    if k or k == 0:
        print(k)
