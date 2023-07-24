"""
Чудо-конвейер

Ввести последовательность объектов Python (только кортежей или целых чисел),
и сымитировать работу Чудо-Конвейера.
Если объект — кортеж, это означает, что на вход конвейеру подаются поочерёдно все объекты из этого кортежа.
Если объект — натуральное число N, это означает, что с выхода конвейера надо снять поочерёдно N объектов,
объединить их в кортеж и вывести.
Если с конвейера нельзя снять N объектов, или в последовательности нет больше команд,
Чудо-Конвейер немедленно останавливается.
"""


s = eval(input())
a = []

for ss in s:
    if type(ss) is tuple:
        a += ss
    elif type(ss) is int:
        if len(a) < ss:
            break
        else:
            print(tuple(a[:ss]))
            a = a[ss:]