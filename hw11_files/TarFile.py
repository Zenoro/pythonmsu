"""
Размер архива

Написать программу, которой на стандартный ввод подаётся tar-архив в виде шестнадцатеричного дампа
(последовательность шестнадцатеричных цифр, возможно, разделённых пробелами и переводами строки),
а на выходе она показывает количество и суммарный объём хранящихся в нём файлов, если их распаковать.
"""


import tarfile
from io import BytesIO
from sys import stdin

dump = bytes.fromhex(stdin.read())
file = BytesIO(dump)
with tarfile.open(fileobj=file) as tararch:
    countres = sum([arfile.isfile() for arfile in tararch])
    sizeres = sum([arfile.get_info()['size'] for arfile in tararch if arfile.isfile()])

print(sizeres, countres)
