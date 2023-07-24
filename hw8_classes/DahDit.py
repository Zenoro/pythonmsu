"""
Морзянка

Написать класс morse("строка"), экземпляр которого переводит арифметические выражения в морзянку!
В выражении «+» — это точка, «-» — тире, а «~» — промежуток между буквами
(бывает только между буквами и только один, проверять не надо).
Параметр — строка, состоящая либо из символов, либо из слов.
Строка состоит из слов, если в ней есть хотя бы один пробел
(в этом случае между словами стоит ровно один пробел)
Если в строке три элемента, они задают точку, точку на конце передаваемой буквы
(традиционно обозначается другим слогом) и тире
Два элемента задают точку и тире, а точка на конце буквы совпадает с обычной
Если элемента четыре, четвёртый — это то, что выводится в конце сообщения
По умолчанию: Если параметров нет, это слова "di", "dit" и "dah".
Если параметры — слова: в конце сообщения выводится ".", разделители при выводе:
пробел между сигналами и ", " между буквами.
Если параметры — символы: непуст только разделитель между буквами (это пробел).
"""


class morse:
    point, endpoint, tire = "", "", ""
    end, space = ".", "_ "
    flaglen = 0

    def __init__(self, args="di dit dah", buf=""):
        self.buf = buf
        if args != "":
            if args[-1] == " ":
                morse.end = args[-1]
            else:
                morse.end = "."
            args = args.split()
            morse.flaglen = len(args)
            if morse.flaglen != 1:
                # not in \'.,;:?!_@-*()%$#
                morse.space = "_ "
            else:
                args = args[0]
                morse.space = " "
                morse.end = "" if morse.end != " " else " "
            morse.point = args[0]
            morse.endpoint = args[0]
            morse.tire = args[1]
            if len(args) > 2:
                morse.endpoint = args[1]
                morse.tire = args[2]
            if len(args) == 4:
                morse.end = args[3]

    def __pos__(self):
        if self.buf == '':
            return morse("", morse.endpoint + " " + self.buf) if morse.flaglen > 1 else morse("", morse.endpoint + self.buf)
        else:
            return morse("", morse.point + " " + self.buf) if morse.flaglen > 1 else morse("", morse.point + self.buf)

    def __neg__(self):
        return morse("", morse.tire + " " + self.buf) if morse.flaglen > 1 else morse("", morse.tire + self.buf)

    def __invert__(self):
        return morse("", morse.space + self.buf)

    def __str__(self):
        if self.buf != "":
            if morse.flaglen > 1:
                self.buf = self.buf.split()
                for k in range(1, len(self.buf)):
                    if self.buf[k-1] == morse.point and self.buf[k] == "_":
                        self.buf[k-1] = morse.endpoint
                return (" ".join(self.buf) + morse.end).replace(' _', ',')
            else:
                self.buf = list(self.buf)
                for i in range(1, len(self.buf)):
                    if self.buf[i-1] == morse.point and self.buf[i] == morse.space:
                        self.buf[i-1] = morse.endpoint
                return "".join(self.buf) + morse.end
        else:
            return self.buf + morse.end
