"""
Лев каренина

https://uneex.org/LecturesCMC/PythonIntro2022/Homework_LevKarenina
"""

from collections import Counter


def output(mas, sss=''):
    if mas == []:
        return "... 0"
    else:
        return mas[0][0]+" "+str(mas[0][1])


u2 = input()
text = ""
while s := input():
    text += " " + s
text = text.split()

res1 = Counter([text[i] for i in range(1, len(text)) if text[i-1][-1] == u2[0] and text[i][0] == u2[1]]).most_common()
res2 = Counter([text[i] for i in range(len(text)) if text[i][0] == u2[2] and text[i][-1] == u2[3]]).most_common()

print(" - ".join([output(res1), output(res2)]))
