"""
Странный класс

Написать класс Nuts, экземпляры которого:
можно конструировать из любого набора объектов (в т. ч. из ничего)
можно индексировать по чему угодно (возвращается объект, который использовался в индексе)
в том числе позволяют присваивать и удалять по индексу (ничего не происходит)
содержат любое поле (возвращается имя этого поля)
в том числе позволяют присваивать и удалять поля (ничего не происходит)
итерируемы (возвращаются строки "N", "u", "t" и "s")
в виде строки представляются как "Nuts"
"""


class Nuts:
    def __init__(self, *args):
        self.x = "Nuts"

    def __str__(self):
        return "Nuts"

    def __iter__(self):
        return iter("Nuts")

    def __getitem__(self, ind):
        return ind

    def __setitem__(self, *args):
        return 0

    def __getattribute__(self, attr):
        return attr

    def __setattribute__(self, *args):
        pass

    def __delitem__(self, b):
        pass

    def __delattr__(self, b):
        pass
