"""
Параметры по умолчанию

Написать метакласс init, который рассчитывает на то, что методы создаваемого им класса полностью аннотированы.
Для каждого позиционного параметра обычного метода в этом классе предусматривается значение по умолчанию
(если оно не было задано) на основании типа в аннотации.
Если в аннотации тип параметра простой, значение по умолчанию — это тип_пареметра()
Если в аннотации тип параметра составной (тип_контейнера[ещё типы], например, list[int]),
    значение по умолчанию — это тип_контейнера()
Если объект соответствующего типа нельзя создать конструктором без операндов, значение по умолчанию — None
"""


import inspect
from sys import stdin


class init(type):
    def __new__(metacls, clsname, clsparent, namespace, **kwargs):
        for i in namespace:
            if inspect.isfunction(namespace[i]):
                signature = inspect.signature(namespace[i])
                dd = {}

                for k, v in signature.parameters.items():
                    if v.default is not inspect.Parameter.empty:
                        dd[k] = v.default
                    elif k != "self":
                        try:
                            dd[k] = namespace[i].__annotations__[k].__call__()
                        except:
                            dd[k] = None

                namespace[i].__defaults__ = tuple(dd.values(),)
                # print(namespace[i].__defaults__)
        return super().__new__(metacls, clsname, clsparent, namespace)


exec(stdin.read())
