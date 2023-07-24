"""
Очередь с фильтром

Напишите класс FilterQueue со следующими свойствами:
1) Это потомок asyncio.Queue
2) В экземпляре класса атрибут очередь.window содержит первый элемент очереди,
    или None, если очередь пуста
3) С помощью операции фильтр in очередь можно определить,
    присутствуют ли в очереди такие элементы, что выражение фильтр(элемент) истинно
4) Метод .later() синхронно переставляет первый элемент очереди в её конец,
    или вызывает исключение asyncio.QueueEmpty, если очередь пуста
5) Метод .get() содержит необязательный параметр фильтр. Вызов очередь.get(фильтр) работает так:
    a) Если в очереди нет элементов, на которых фильтр(элемент) истинно, работает как обычный .get().
    b) Если в очереди есть элементы, на которых фильтр(элемент) истинно,
    переставляет первый элемент очереди в её конец до тех пор, пока фильтр(элемент) не истинно,
    а затем выполняет обычный .get().
Разрешается воспользоваться внутренним представлением Queue
"""


import asyncio
import sys


class FilterQueue(asyncio.Queue):
    def __init__(self, k=0):
        super().__init__(k)

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        else:
            k = self.__dict__['_queue'].popleft()
            self.__dict__['_queue'].append(k)

    def get(self, fil=lambda x: 0):
        buf = self.__dict__['_queue'].copy()
        for d in buf:
            if fil(d):
                return super().get()
            else:
                k = self.__dict__['_queue'].popleft()
                self.__dict__['_queue'].append(k)
        return super().get()

    @property
    def window(self):
        return self.__dict__['_queue'][0]


exec(sys.stdin.read())
