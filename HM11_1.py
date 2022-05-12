"""Реализована последовательность Фибоначи при помощи генератора/итератора"""
"""Использование простейших регулярных выражений"""
"""Уважаемый ментор, прошу вас простить неродивого студента, у которого скоро сессия, более сложную задачу по регулярным выражениям отправлю вам позже."""

import re


def fib(n: int):
    """Реализация последовательности Фибоначи с помощью генератора"""
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


d = fib(7)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))


class Fib:

    def __init__(self, n):
        self.n = n
        self.current = 0
        self.f1 = 0
        self.f2 = 1

    def __iter__(self):
        return self

    def __str__(self):
        return f'Реализация последовательности Фибоначи через итератор с помощью ООП.'

    def __next__(self):

        self.f1, self.f2 = self.f2, self.f1 + self.f2

        if self.current < self.n:
            self.current += 1
            return self.f1
        else:
            raise StopIteration


for i in Fib(9):
    print(i, end='  ')


def time(s: str) -> bool:
    """Опрделеляет время, заданное строкой, на корректность."""
    pattern = r'[0-2][0-4]\:[0-5][0-9]'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False


print(time('23:56'))
