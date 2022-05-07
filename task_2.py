"""Домашнее задание, пункт номер 2"""

from dataclasses import dataclass
import dataclasses
import json

with open('data.json', 'r') as file:
    data = json.load(file)

MyClass_2 = type('MyClass_2', (), data)


@dataclass
class MyClass(MyClass_2):
    def show(self):
        x = MyClass_2()
        for attr in dir(x):
            if attr[0] != '_':
                print(getattr(x, attr), '\n')


d = MyClass()
d.show()