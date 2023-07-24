"""
Хранилище объектов

Написать функцию sloter(fields, default), которой передаётся последовательность полей fields,
и значение по умолчанию default, а возвращает она класс,
в экземпляре которого все эти поля есть, равны указанному значению и способны хранить произвольные объекты.
Попытки создать другие поля в этом экземпляре должны приводить к исключению AttributeError.
При проходе циклом экземпляр возвращает поля в порядке их объявления.
"""


def sloter(fields, default):
    class C:
        __slots__ = fields

        def __init__(self, val=default):
            for i in self.__slots__:
                setattr(self, i, val)

        def __iter__(self):
            return iter(getattr(self, i) for i in self.__slots__)

        def __delattr__(self, name: str):
            setattr(self, name, default)
    return C
