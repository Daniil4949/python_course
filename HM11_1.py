"""Реализована последовательность Фибоначи при помощи генератора/итератора"""


def fib(n):
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

    def __next__(self):
        self.f1, self.f2 = self.f2, self.f1 + self.f2

        if self.current < self.n:
            self.current += 1
            return self.f1
        else:
            raise StopIteration


for i in Fib(9):
    print(i, end='  ')
