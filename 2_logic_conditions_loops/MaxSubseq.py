"""
Длиннейшая подпоследовательность

Вводить по одному непустую последовательность целых чисел, не равных нулю.
Ноль означает конец в вода и не учитывается.
Вывести наибольшую длину неубывающей подпоследовательности
подряд идущих чисел исходной последовательности.
Хранить введённую последовательность
или её невырожденную подпоследоватиельность запрещается.
"""


counter = counterres = 1
integer1 = int(input())
while (integ := int(input())) != 0:
    if integer1 <= integ:
        counter += 1
        integer1 = integ
    else:
        if counterres < counter:
            counterres = counter
        counter = 1
        integer1 = integ
print(counter if counterres < counter else counterres)
